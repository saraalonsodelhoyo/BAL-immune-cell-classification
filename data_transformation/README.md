# Data Transformation Tools

This folder contains scripts and notebooks used to **prepare and convert data annotations** for training YOLO models on BAL images.

---

## `create_yolo_annotations.ipynb`

Jupyter notebook used at the start of the project to convert **segmentation masks** into **YOLO-format bounding box labels**.

### It performs:
- Reading gray-scale mask images.
- Extracting contours and computing bounding boxes.
- Saving YOLO-format `.txt` annotation files.

Use this if your data is in **segmentation format** (masks per class).

---

## `geojson_2_yolo.py`

Converts labels in **GeoJSON** format into YOLO `.txt` files.

- Input: `.geojson` annotation files with labeled objects.
- Output: `.txt` YOLO annotations (class, x_center, y_center, width, height).
- Supports batch processing of multiple files.

---

## `yolo_2_geojson.py`

Converts YOLO `.txt` label files back into **GeoJSON format**.

Useful for:
- Visualization in annotation tools like QuPath.
- Debugging or exporting predictions in a more standard format.

---

## Notes

- All scripts expect specific folder structures - update paths as needed before use.
- Requires basic packages like `opencv-python`, `shapely`, `numpy`.

