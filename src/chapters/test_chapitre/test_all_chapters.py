"""
Test runner for all chapter modules.
This script imports each chapter module in `src.chapters` and calls its main/start function when available.
All user inputs are answered with "1" automatically to allow headless testing.
"""
import builtins
import importlib
import inspect
import sys
import traceback

# Mock input to always return "1"
def _mock_input(prompt=''):
    # print the prompt and the mock reply to make logs readable
    if prompt:
        # Keep same line behavior as interactive input
        print(prompt, end='')
    print("1")
    return "1"

builtins.input = _mock_input

# Patch keyboard.wait if module uses it
try:
    import keyboard as _keyboard
    _keyboard.wait = lambda *a, **k: None
except Exception:
    # keyboard may not be installed or used; ignore
    pass

# Also patch wait_for_enter in input_utils if present
try:
    from src.utils import input_utils as iu
    if hasattr(iu, 'wait_for_enter'):
        iu.wait_for_enter = lambda: None
except Exception:
    pass

# Helper to create a character when needed
def get_test_character():
    try:
        from src.utils.input_utils import charger_personnage
    except Exception:
        # fallback: try to construct a minimal Character
        charger_personnage = None

    if charger_personnage:
        try:
            return charger_personnage()
        except Exception:
            pass

    try:
        from src.universe.character import Character
        # create a basic character
        attrs = { 'courage': 5, 'intelligence': 5, 'loyalty': 5, 'ambition': 5 }
        return Character('Test','Player', attrs)
    except Exception:
        return None


modules = [
    'src.chapters.chapter_1',
    'src.chapters.chapter_2',
    'src.chapters.chapter_3',
    'src.chapters.chapter_4',
    'src.chapters.chapter_5_extension'
]

results = {}
char = None

for mod_name in modules:
    print(f"\n--- Testing {mod_name} ---")
    try:
        mod = importlib.import_module(mod_name)
    except Exception:
        traceback.print_exc()
        results[mod_name] = 'import failed'
        continue

    # find callable candidates
    called = False
    # prefer explicit start_* functions
    for attr in dir(mod):
        if attr.startswith('start_chapter') or attr.startswith('start') or attr == 'main' or attr == 'run':
            fn = getattr(mod, attr)
            if callable(fn):
                try:
                    sig = inspect.signature(fn)
                    params = len(sig.parameters)
                    if params == 0:
                        fn()
                    elif params == 1:
                        if not char:
                            char = get_test_character()
                        fn(char)
                    else:
                        # try calling with character and ignore extras
                        if not char:
                            char = get_test_character()
                        try:
                            fn(char)
                        except Exception:
                            fn()
                    called = True
                    print(f"Called {attr}() successfully")
                    break
                except Exception:
                    traceback.print_exc()
                    results[mod_name] = f"call {attr} failed"
                    called = True
                    break

    if called:
        if mod_name not in results:
            results[mod_name] = 'ok'
        continue

    # fallback: look for known functions
    if hasattr(mod, 'learn_spells'):
        try:
            if not char:
                char = get_test_character()
            mod.learn_spells(char)
            results[mod_name] = 'learn_spells ok'
            continue
        except Exception:
            traceback.print_exc()
            results[mod_name] = 'learn_spells failed'
            continue

    results[mod_name] = 'no callable found'

print('\n--- Summary ---')
for k, v in results.items():
    print(f'{k}: {v}')
