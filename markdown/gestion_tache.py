import json

with open("taches.json") as f:
    tasks = json.load(f)

summary = {}
for task in tasks:
    print(task)
    person = task["assigne"]
    summary.setdefault(person, []).append(f"- {task['tache']} [{task['statut']}]")

md = "# Récapitulatif par personne\n\n"
for person, taches in summary.items():
    md += f"## {person}\n"
    for t in taches:
        md += t + "\n"
    md += "\n"

with open("../TODO_SUMMARY.md", "w") as f:
    f.write(md)
