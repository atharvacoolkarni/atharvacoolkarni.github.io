import json
from pathlib import Path

path = Path("assets/projects/flight_analysis/plots/q5/q5_ml_analysis.json")

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)

step = 100

for model, curve in data["roc_curves"].items():
    curve["fpr"] = curve["fpr"][::step]
    curve["tpr"] = curve["tpr"][::step]

new_path = Path("assets/projects/flight_analysis/plots/q5/q5_ml_analysis_small.json")

with new_path.open("w", encoding="utf-8") as f:
    json.dump(data, f)

print(f"Saved to {new_path}")