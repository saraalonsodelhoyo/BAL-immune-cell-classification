import os
import json
from pathlib import Path

# === CONFIGURATION ===
IMAGE_SIZE = 512
INPUT_DIR = Path("outputs/inference_results/predicted_labels")
OUTPUT_DIR = Path("outputs/inference_results/geojson_annotations")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Class map: class_id → (class_name, colorRGB)
CLASS_MAP = {
    0: ("Macrophage", -16776961),    # Green
    1: ("Lymphocyte", -16711936),    # Blue
    2: ("PMN Cell", -65281),         # Magenta
    3: ("Eosinophile", 8421376),     # Olive
}

# === CONVERSION LOOP ===
for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".txt"):
        continue

    features = []
    input_path = INPUT_DIR / filename

    with open(input_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue

            class_id, x_center, y_center, width, height = map(float, parts)
            class_id = int(class_id)

            # Convert normalized coordinates to absolute
            x_center *= IMAGE_SIZE
            y_center *= IMAGE_SIZE
            width *= IMAGE_SIZE
            height *= IMAGE_SIZE

            x_min = x_center - width / 2
            y_min = y_center - height / 2
            x_max = x_center + width / 2
            y_max = y_center + height / 2

            polygon = [
                [x_min, y_min],
                [x_min, y_max],
                [x_max, y_max],
                [x_max, y_min],
                [x_min, y_min]
            ]

            class_name, color = CLASS_MAP.get(class_id, ("unknown", -1))

            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [polygon]
                },
                "properties": {
                    "object_type": "annotation",
                    "classification": {
                        "name": class_name,
                        "colorRGB": color
                    },
                    "isLocked": False
                }
            }

            features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    output_filename = Path(filename).stem + ".geojson"
    output_path = OUTPUT_DIR / output_filename

    with open(output_path, "w") as out_f:
        json.dump(geojson, out_f, indent=2)

    print(f"Saved: {output_path}")