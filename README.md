# YOLOLab

<img src="https://github.com/phiflip/YOLOLab/blob/main/icons/YOLOv8Lab_final_icon_nobackgorund_highRes.png" width="150" alt="YOLOLab logo">

YOLOLab provides a simple setup for labeling, training, evaluating, and using Ultralytics YOLO object detection models in educational settings.

The examples in this README use **Ultralytics YOLO26**. YOLOLab originally used YOLOv8; the current commands and model names follow the [Ultralytics documentation](https://docs.ultralytics.com/).

## Table of Contents

1. [Installation](#installation)
2. [Labeling](#labeling)
3. [Training](#training)
4. [Predictions](#predictions)
5. [Evaluation](#evaluation)
6. [Tracking](#tracking)
7. [References](#references)

## Installation

The following instructions assume **Windows**, **Anaconda**, and **Spyder**. CLI commands are run in an **Anaconda Prompt**, after activating the `yolo` environment. For installation, use `pip install` directly; `python -m pip` is not required.

### Prerequisites

- [Anaconda](https://www.anaconda.com/download)
- Python 3.12 (installed in the environment below)
- Optional: an NVIDIA GPU with a CUDA-enabled PyTorch installation for faster training

### Project directory

Create a local working directory, for example:

```text
C:/Users/UserName/yolo/
├── labeling/
├── complete_dataset/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   └── data.yaml
├── training_runs/
├── predictions/
└── tracking_runs/
```

`UserName` is a placeholder. Replace it with your Windows username in the commands below.

### Environment setup (Anaconda Prompt)

1. **Create the environment:**

   ![Anaconda Prompt](https://github.com/phiflip/YOLOLab/blob/main/icons/anaconda_prompt_snippet.PNG)

   ```bash
   conda create --name yolo python=3.12 spyder=6 -y
   ```

2. **Activate it:**

   ```bash
   conda activate yolo
   ```

3. **Install or update Ultralytics:**

   ```bash
   pip install -U ultralytics
   ```

4. **Check the installation:**

   ```bash
   yolo checks
   ```

   `yolo checks` displays the installed software and available compute devices. For NVIDIA GPU support, follow the [PyTorch installation instructions](https://pytorch.org/get-started/locally/) if CUDA is not detected.

5. **Start Spyder (optional):**

   ```bash
   spyder
   ```

   Alternatively, open and run [scripts/yolo_test.py](https://github.com/phiflip/YOLOLab/blob/main/scripts/yolo_test.py) in Spyder. Older repository scripts may still refer to previous YOLO models.

### Quick test from the CLI

Predict objects in a sample image:

```bash
yolo detect predict model=yolo26n.pt source="https://ultralytics.com/images/bus.jpg"
```

Use a webcam (press `q` to close the video window):

```bash
yolo detect predict model=yolo26n.pt source=0 show=True
```

The pretrained weights are downloaded automatically when first used.

## Labeling

### Install Label Studio

With the `yolo` environment activated:

```bash
pip install label-studio
label-studio
```

Open <http://localhost:8080> and create an account on first launch.

### Use a local folder

For labeling, copy the supplied images to a local directory, for example:

```text
C:/labeling/Lastname_Firstname/
```

Avoid network/UNC paths and OneDrive-synchronized folders. Depending on Windows settings, `Desktop`, `Documents`, and `Downloads` may also be synchronized.

Before training, export or convert annotations to the **Ultralytics YOLO detection format** and check the class IDs and image/label pairs.

## Training

Training uses a **pretrained YOLO26 detection model** (transfer learning). Start with the nano model, `yolo26n.pt`.

### 1. Prepare the dataset

Use the directory structure shown under [Project directory](#project-directory). Each labeled image must have a matching `.txt` file in its corresponding `labels/` folder.

Example:

```text
complete_dataset/train/images/image001.jpg
complete_dataset/train/labels/image001.txt
```

Each line in a detection label file has the format:

```text
class_id x_center y_center width height
```

Coordinates must be normalized to the range `[0, 1]`. Class IDs start at `0`. Images without objects may have an empty label file or no label file.

Recommended split for this course: **70% train, 20% validation, 10% test**. Keep related or near-duplicate images in the same split to avoid data leakage.

### 2. Configure `data.yaml`

Save this file as `C:/Users/UserName/yolo/complete_dataset/data.yaml`:

```yaml
path: C:/Users/UserName/yolo/complete_dataset
train: train/images
val: valid/images
test: test/images

names:
  0: boar
  1: human
```

Replace the example class names with the classes in **your dataset**. `path` must match your local dataset directory.

**Important:** `val` is the YAML key used by Ultralytics even when the physical folder is named `valid`.

### 3. Train using the CLI

Run in an **Anaconda Prompt** with `conda activate yolo` (no `python -m` prefix):

```bash
yolo detect train model=yolo26n.pt data="C:/Users/UserName/yolo/complete_dataset/data.yaml" epochs=100 imgsz=640 batch=8 device=cpu project="C:/Users/UserName/yolo/training_runs" name=yolo26n_imgsz640
```

For an NVIDIA GPU with CUDA-enabled PyTorch, replace `device=cpu` with `device=0`.

Training outputs are saved in:

```text
C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/
├── weights/
│   ├── best.pt
│   └── last.pt
└── ...
```

`best.pt` contains the checkpoint selected using validation performance (for object detection, by default **mAP@0.5:0.95**). `last.pt` is the last training checkpoint.

### 4. Train using Python (Spyder)

```python
from ultralytics import YOLO


def main():
    model = YOLO("yolo26n.pt")
    model.train(
        data="C:/Users/UserName/yolo/complete_dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device="cpu",  # Use 0 for an NVIDIA CUDA GPU
        project="C:/Users/UserName/yolo/training_runs",
        name="yolo26n_imgsz640",
    )


if __name__ == "__main__":
    main()
```

The `if __name__ == "__main__":` guard is recommended for training scripts on Windows because of multiprocessing.

### Main training parameters

| Parameter | Meaning |
| --- | --- |
| `model=yolo26n.pt` | Pretrained YOLO26 nano detection model. Larger variants include `yolo26s.pt`, `yolo26m.pt`, `yolo26l.pt`, and `yolo26x.pt`. |
| `data=...` | Path to the dataset `data.yaml`. |
| `epochs=100` | Maximum number of training epochs. Early stopping may end training sooner. |
| `imgsz=640` | Input image size in pixels. |
| `batch=8` | Number of images per training batch. Reduce this if GPU memory is insufficient. |
| `device=cpu` / `device=0` | Train on the CPU or the first CUDA GPU. |
| `project=...` | Parent directory for saved runs. |
| `name=...` | Name of the training run. |

For more options, see [Ultralytics training settings](https://docs.ultralytics.com/modes/train/#train-settings). For object detection, `dropout` is **not** the usual tuning parameter; the documented `dropout` setting applies to classification.

### Optional: real-time experiment logging (Weights & Biases)

In the activated Anaconda Prompt:

```bash
pip install wandb
wandb login
yolo settings wandb=True
```

Start the normal training command afterward. To disable W&B logging, use `yolo settings wandb=False`. See the [Ultralytics W&B integration](https://docs.ultralytics.com/integrations/weights-biases/).

## Predictions

Use the trained `best.pt` checkpoint for object detection on images, folders, videos, or a webcam. **Prediction does not calculate accuracy metrics**; use [Evaluation](#evaluation) for that.

### CLI

```bash
yolo detect predict model="C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt" source="C:/Users/UserName/yolo/complete_dataset/test/images" conf=0.2 imgsz=640 save=True project="C:/Users/UserName/yolo/predictions" name=yolo26n_imgsz640
```

### Python

```python
from ultralytics import YOLO
import matplotlib.pyplot as plt

model = YOLO("C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt")

results = model.predict(
    source="C:/Users/UserName/yolo/complete_dataset/test/images",
    conf=0.2,
    imgsz=640,
    save=True,
    project="C:/Users/UserName/yolo/predictions",
    name="yolo26n_imgsz640",
)

# Show the first predicted image in Matplotlib.
if results:
    image_bgr = results[0].plot()
    plt.imshow(image_bgr[:, :, ::-1])
    plt.axis("off")
    plt.show()
```

## Evaluation

**Validation (`val`)** is used while training and selecting a model. The independent **test set (`test`)** should be evaluated after training and model selection are complete. Test images must not have been used for training or validation.

### CLI: evaluate the test set

```bash
yolo detect val model="C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt" data="C:/Users/UserName/yolo/complete_dataset/data.yaml" split=test imgsz=640 plots=True
```

To evaluate the validation split instead, set `split=val`.

### Python: metrics and precision-recall plots

```python
from ultralytics import YOLO

model = YOLO("C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt")

metrics = model.val(
    data="C:/Users/UserName/yolo/complete_dataset/data.yaml",
    split="test",
    imgsz=640,
    plots=True,
)

print(f"Mean precision:   {metrics.box.mp:.4f}")
print(f"Mean recall:      {metrics.box.mr:.4f}")
print(f"mAP@0.5:          {metrics.box.map50:.4f}")
print(f"mAP@0.5:0.95:     {metrics.box.map:.4f}")
```

Ultralytics saves evaluation plots, including the precision-recall curve, when `plots=True`. The `metrics.box` values are **detection/bounding-box metrics**. Do not confuse the evaluation metric `mAP@0.5` with the prediction confidence threshold `conf` or the non-maximum suppression threshold `iou`.

See [Ultralytics validation documentation](https://docs.ultralytics.com/modes/val/).

## Tracking

Tracking assigns IDs to detected objects across **video frames**. Use a video file, live stream, or webcam; a folder of unrelated images is not a useful tracking example.

### CLI

```bash
yolo detect track model="C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt" source="C:/Users/UserName/yolo/video.mp4" tracker=botsort.yaml conf=0.2 imgsz=640 save=True project="C:/Users/UserName/yolo/tracking_runs" name=yolo26n_botsort
```

### Python

```python
from ultralytics import YOLO

model = YOLO("C:/Users/UserName/yolo/training_runs/yolo26n_imgsz640/weights/best.pt")

model.track(
    source="C:/Users/UserName/yolo/video.mp4",
    tracker="botsort.yaml",
    conf=0.2,
    imgsz=640,
    save=True,
    project="C:/Users/UserName/yolo/tracking_runs",
    name="yolo26n_botsort",
)
```

For tracker configuration files and additional examples, see [YOLOLab Tracking scripts](https://github.com/phiflip/YOLOLab/tree/main/scripts/Tracking) and the [Ultralytics tracking documentation](https://docs.ultralytics.com/modes/track/).

## References

YOLOLab is based on the [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) software project. The original YOLOLab documentation cited Jocher, G., Chaurasia, A., & Qiu, J. (2023), *Ultralytics YOLO* (version 8.0.0). The training and inference examples above now target **YOLO26**, not YOLOv8.

- [Ultralytics YOLO26 models](https://docs.ultralytics.com/models/yolo26/)
- [Ultralytics CLI](https://docs.ultralytics.com/usage/cli/)
- [Object detection dataset format](https://docs.ultralytics.com/datasets/detect/)
- [Training](https://docs.ultralytics.com/modes/train/)
- [Prediction](https://docs.ultralytics.com/modes/predict/)
- [Validation](https://docs.ultralytics.com/modes/val/)
- [Tracking](https://docs.ultralytics.com/modes/track/)

Documentation checked against the Ultralytics online documentation on **19 October 2026**. All command-line examples assume an activated Anaconda environment.
