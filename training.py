import os
import argparse
import wandb
from pathlib import Path
from ultralytics import YOLO

# === CONFIGURATION ===
BASE_DIR = Path("data/datasets")              # e.g., data/datasets/no_aug/
MODEL_PATH = Path("models/yolov12n.pt")       # Pretrained YOLO model
OUTPUT_DIR = Path("runs/yolov12n_training")   # Where to save training results

def train_yolo(dataset_name: str):
    """
    Train YOLO using a dataset located in BASE_DIR/dataset_name
    """

    # Resolve paths
    dataset_path = BASE_DIR / dataset_name
    train_dir = dataset_path / "images/train"
    val_dir = dataset_path / "images/val"
    yaml_path = dataset_path / "cell_detection.yaml"

    # Validate input paths
    if not BASE_DIR.exists():
        raise FileNotFoundError(f"Base dataset directory not found: {BASE_DIR}")
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    if not train_dir.exists() or not val_dir.exists():
        raise FileNotFoundError(f"Missing train/val images in: {dataset_path}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create YAML config for YOLO training
    yaml_content = f"""
    train: {train_dir}
    val: {val_dir}
    nc: 4
    names: ['macrophages', 'lymphocytes', 'polymorphonuclear cells', 'eosinophils']
    """
    with open(yaml_path, "w") as f:
        f.write(yaml_content.strip())

    # Load YOLO model
    model = YOLO(str(MODEL_PATH))

    # Training configuration
    model_version = "yolov12n"
    augm = False
    epochs = 60
    seed = 0
    run_name = model_version

    # Initialize Weights & Biases
    wandb.init(
        project="yolo-training",
        name=run_name,
        config={
            "dataset": dataset_name,
            "data_augmentation": augm,
            "model_version": model_version,
            "epochs": epochs,
            "seed": seed,
        }
    )

    # Train YOLO model
    model.train(
        data=str(yaml_path),
        epochs=epochs,
        imgsz=512,
        batch=64,
        workers=3,
        seed=seed,
        project=str(OUTPUT_DIR),
        name=run_name,

        # Default augmentation techniques disabled (augm = False)
        translate=0.0,
        scale=0.0,
        shear=0.0,
        fliplr=0.0,
        flipud=0.0,
        degrees=0.0,
        hsv_h=0.0,
        hsv_s=0.0,
        hsv_v=0.0,
        mosaic=0.0,
        mixup=0.0,
        erasing=0.0,
        auto_augment=None,
    )

    wandb.finish()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train YOLOv8 with a dataset.")
    parser.add_argument("dataset_name", type=str, help="Dataset folder inside data/datasets/")

    args = parser.parse_args()
    train_yolo(args.dataset_name)