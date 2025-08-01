import os
import json
from pathlib import Path

# === CONFIGURATION ===
IMAGE_SIZE = 512
INPUT_DIR = Path("data/geojson_annotations")
OUTPUT_DIR = Path("data/yolo_labels")

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Class mapping
CLASS_NAME_TO_ID = {
    "Macrophage": 0,
    "Lymphocyte": 1,
    "PMN Cell": 2,
    "Eosinophil": 3,
}

# === CONVERSION LOOP ===
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".geojson"):
        continue

    input_path = INPUT_DIR / filename
    output_filename = Path(filename).stem + ".txt"
    output_path = OUTPUT_DIR / output_filename

    with open(input_path, "r") as f:
        data = json.load(f)

    lines = []
    for feature in data.get("features", []):
        geometry = feature.get("geometry", {})
        properties = feature.get("properties", {})

        if geometry.get("type") != "Polygon":
            continue

        coords = geometry.get("coordinates", [])
        if not coords or not coords[0]:
            continue

        polygon = coords[0]
        xs = [pt[0] for pt in polygon]
        ys = [pt[1] for pt in polygon]

        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        x_center = (x_min + x_max) / 2 / IMAGE_SIZE
        y_center = (y_min + y_max) / 2 / IMAGE_SIZE
        width = (x_max - x_min) / IMAGE_SIZE
        height = (y_max - y_min) / IMAGE_SIZE

        class_name = properties.get("classification", {}).get("name", "unknown")
        class_id = CLASS_NAME_TO_ID.get(class_name)

        if class_id is None:
            print(f"Warning: Unknown class '{class_name}' in {filename}, skipping.")
            continue

        lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    with open(output_path, "w") as out_f:
        out_f.write("\n".join(lines))

    print(f"Saved: {output_path}")