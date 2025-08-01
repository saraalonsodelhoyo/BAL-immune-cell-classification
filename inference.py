import os
import cv2
import shutil
from pathlib import Path
from ultralytics import YOLO

# === CONFIGURATION ===
MODEL_PATH = Path("models/best.pt")
INPUT_FOLDER = Path("data/input_images")
OUTPUT_FOLDER = Path("outputs/inference_results")

# Output subfolders
IMAGES_OUT = OUTPUT_FOLDER / "predicted_images"
LABELS_OUT = OUTPUT_FOLDER / "predicted_labels"
COPIED_IMAGES_OUT = OUTPUT_FOLDER / "source_images"

# Create output folders if they don't exist
IMAGES_OUT.mkdir(parents=True, exist_ok=True)
LABELS_OUT.mkdir(parents=True, exist_ok=True)
COPIED_IMAGES_OUT.mkdir(parents=True, exist_ok=True)

# Class info
CLASS_COLORS = {
    0: (0, 255, 0),    # Macrophages - Green
    1: (255, 0, 0),    # Lymphocytes - Blue
    2: (0, 0, 255),    # Polymorphonuclear cells - Red
    3: (128, 128, 0),  # Eosinophils - Olive
}

CLASS_NAMES = {
    0: "Macrophages",
    1: "Lymphocytes",
    2: "Polymorphonuclear",
    3: "Eosinophils"
}

def draw_predictions(image, results):
    for box, cls_id in zip(results[0].boxes.xywh, results[0].boxes.cls):
        x_center, y_center, w, h = map(float, box)
        xmin = int(x_center - w / 2)
        ymin = int(y_center - h / 2)
        xmax = int(x_center + w / 2)
        ymax = int(y_center + h / 2)

        cls = int(cls_id.item())
        color = CLASS_COLORS.get(cls, (255, 255, 255))
        label = CLASS_NAMES.get(cls, f"Class {cls}")

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.putText(image, label, (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image

def save_labels_yolo_format(results, label_output_path, img_width, img_height):
    with open(label_output_path, 'w') as f:
        for box, cls_id in zip(results[0].boxes.xywh, results[0].boxes.cls):
            x_center, y_center, w, h = map(float, box)
            x_center /= img_width
            y_center /= img_height
            w /= img_width
            h /= img_height
            cls = int(cls_id.item())
            f.write(f"{cls} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

def perform_inference():
    print("Starting inference...")

    model = YOLO(str(MODEL_PATH))

    image_paths = list(INPUT_FOLDER.glob("*.png"))
    print(f"Found {len(image_paths)} images in {INPUT_FOLDER}")

    for image_path in image_paths:
        print(f"\nProcessing image: {image_path.name}")
        image = cv2.imread(str(image_path))
        if image is None:
            print(f"Could not read image {image_path}. Skipping...")
            continue

        image_resized = cv2.resize(image, (512, 512))
        results = model.predict(source=image_resized, agnostic_nms=True)
        image_with_predictions = draw_predictions(image_resized.copy(), results)

        output_image_path = IMAGES_OUT / image_path.name
        label_output_path = LABELS_OUT / (image_path.stem + ".txt")
        copied_image_path = COPIED_IMAGES_OUT / image_path.name

        cv2.imwrite(str(output_image_path), image_with_predictions)
        save_labels_yolo_format(results, str(label_output_path), 512, 512)
        shutil.copy(str(image_path), str(copied_image_path))

        print(f"Saved predicted: {output_image_path}")
        print(f"Saved label:    {label_output_path}")
        print(f"Copied source:  {copied_image_path}")

    print("\nInference complete.")

if __name__ == "__main__":
    perform_inference()