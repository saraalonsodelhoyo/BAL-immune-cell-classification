# Trained Models

This folder is intended to store **trained YOLO model weights** for inference and evaluation.

> **Note:** Model files are **not included** in this repository due to file size limitations.

---

## Download Trained Weights

You can download the trained models from the following Google Drive folder:

**[Model weights – Google Drive](https://drive.google.com/drive/folders/1--A-mW5Y3dX8wpkTLbM-bX8rf6rylmxl?usp=drive_link)**

Place the downloaded `.pt` files in this folder (i.e., `my-yolo-bal-project/models/`).

---

## Example Files

| Filename           | YOLO Version | Dataset | Epochs | Notes                  |
|--------------------|--------------|---------|--------|------------------------|
| `best_yolo12n.pt`  | YOLOv12n     | dataset | 100    | Custom hyperparameters |
| `best_yolo12x.pt`  | YOLOv12x     | dataset | 100    | Default hyperparams    |

---

## Folder Usage

```python
models/
├── best_yolo12n.pt
├── best_yolo12x.pt
└── README.md
```

---

## How to Use

To run inference with any of the trained models using SLURM, submit the job with:

```python
sbatch scripts/run_inference.sh
```

Make sure that inference.py contains the correct data and model paths in lines:

```python
MODEL_PATH = Path("models/best.pt")
INPUT_FOLDER = Path("data/input_images")
```
