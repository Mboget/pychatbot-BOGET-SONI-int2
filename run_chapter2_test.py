#!/usr/bin/env python
import sys
import os

# Ajouter les inputs
inputs = ["1", "1", "1", "1", "1", ""]
input_index = 0

# Overrider input()
original_input = input
def mock_input(prompt=""):
    global input_index
    if prompt:
        print(prompt, end="", flush=True)
    if input_index < len(inputs):
        val = inputs[input_index]
        input_index += 1
        print(val)
        return val
    raise EOFError()

import builtins
builtins.input = mock_input

# Lancer chapter_2
from src.chapters.chapter_2 import charger_personnage, start_chapter_2

perso = charger_personnage()
start_chapter_2(perso)
