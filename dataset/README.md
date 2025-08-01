# Dataset Folder

This folder defines the expected **data structure** for training and evaluation using YOLO models on BAL (Bronchoalveolar Lavage) cell images.

> **Note:** The dataset is not stored in this repository due to size limitations.

---

## Download Dataset

You can download the dataset from the following Google Drive folder:

**[Data – Google Drive](https://drive.google.com/drive/folders/1jzIaSdwMp5ZQKIjxjruXzNyv1CUVvtb-?usp=drive_link)**

After downloading, place the files into this `dataset/` folder, maintaining the following structure.

---

## Expected Directory Layout

```python
dataset/
├── images/
│ ├── train/ # Training images (.jpg or .png)
│ └── val/ # Validation images
├── labels/
│ ├── train/ # YOLO-format label files (.txt)
│ └── val/ # Validation labels
```

Each image in `images/train` or `images/val` must have a corresponding `.txt` annotation file in the `labels/train` or `labels/val` directory with the **same filename** (but `.txt` extension).

---

## YOLO Label Format

Each `.txt` file contains lines like the following:

```bash
<class_id> <x_center> <y_center> <width> <height>
```


Where:
- `class_id`: integer index of the class (e.g., 0, 1, 2…)
- Coordinates are **normalized** between 0 and 1
  - `x_center`, `y_center`: object center (relative to image width and height)
  - `width`, `height`: size of the bounding box

---

## Auto-generated YAML

During training, the following YAML file is auto-created by `train.py`:

```bash
cell_detection.yaml
```

Example content:

```yaml
train: dataset/images/train
val: dataset/images/val
nc: 4
names: ['macrophages', 'lymphocytes', 'polymorphonuclear cells', 'eosinophils']
```

This YAML file defines the dataset config for the YOLO training pipeline.