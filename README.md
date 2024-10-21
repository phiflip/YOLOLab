# YOLOv8Lab
<img src="https://github.com/phiflip/YOLOv8Lab/blob/main/icons/YOLOv8Lab_final_icon_nobackgorund_highRes.png" width="150" alt="YOLOv8Lab main logo type">

Welcome to the YOLOv8Lab repository, a dedicated platform for setting up and using YOLOv8 for object detection tasks in educational settings.
<br />
<br />
This repository and code is based on the YOLOv8 project by: Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0)
[Computer software]. https://github.com/ultralytics/ultralytics

# Table of Contents

1. [Installation](#installation)
2. [Labeling](#labeling)
3. [Training](#training)
4. [Predictions](#predictions)
5. [Tracking](#tracking)



## Installation

This project assumes that Anaconda and Spyder are installed on your Windows system. Follow the steps below to set up your environment.

### Prerequisites

- Anaconda: Download and install Anaconda from the [official website](https://www.anaconda.com/products/individual).
  See installation guides for different operating systems:
   - [Installing on Windows](https://docs.anaconda.com/free/anaconda/install/windows/),
   - [Installing on Linux](https://docs.anaconda.com/free/anaconda/install/linux/),
   - [Installing on macOS](https://docs.anaconda.com/free/anaconda/install/mac-os/).
- Python >= 3.9 (comes with Anaconda)

### Directory structure

1. **Create the yolov8 project folder**
```bash
C:/
├─ Users
│   ├─ UserName
│   │   ├─ yolov8                  
│   │   │   ├─ labeling/        
│   │   │   ├─ train/
│   │   │   ├─ test/     
│   │   │   └─ valid/
│   │   └─ ...             
│   └─ ...
└──...
```
### Environment Setup (via Anaconda Prompt)

2. **Create a new conda environment (in the windows search bar type "Anaconda Prompt"):**
   <kbd> <img src="https://github.com/phiflip/YOLOv8Lab/blob/main/icons/anaconda_prompt_snippet.PNG" width="500" alt="Prompt"></kbd>

   ```bash
   conda create --name yolov8 python=3.9 spyder=5
   ```

3. **Activate the environment:**
   ```bash
   conda activate yolov8
   ```

5. **Install Required Packages:**
   ```bash
   pip install ultralytics
   ```

6. **Launch Spyder within the new environment:**
   ```bash
   spyder
   ```
7. **… and check your installation by opening and running the yolov8_test.py in Spyder:**
   
   [Download yolov8_test.py](https://github.com/phiflip/YOLOv8Lab/blob/main/scripts/yolov8_test.py)
8. **... or by typing the following commads in your Command Line Interface (CLI):**
    #### Predict on an image
    ```bash
    yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
    ```

    #### Run a pretrained yolo object detector on your webcam
   ```bash
   yolo predict model=yolov8n.pt source=0 show=True
   ```
   

## Labeling
### Additional Tools

1. **Install labelImg for image annotation using the same activated yolov8 environment:**
   ```bash
   conda install -c conda-forge labelimg
   ```
2. **Start the labeling software:**
   ```bash
   labelimg 
   ```
3. **... in the correct folder (labelImg [path to images] [path to predefined_classes.txt file]):**
   ```bash
   labelimg C:\Users\UserName\yolov8\labeling C:\Users\UserName\yolov8\labeling\predefined_classes.txt 
   ```   
   <kbd><img src="https://github.com/phiflip/YOLOv8Lab/blob/main/icons/labelimg_startup.png" width="500"  border="1px solid red" alt="LabelImg"></kbd>
  

## Training

### Start a Training on your local machine directly in the **CLI** ...


```bash
yolo task=detect mode=train model=yolov8n.pt imgsz=800 data=path/to/boars.yaml epochs=200 batch=8 project=/path/to/your/project/training_runs/ name=yolov8n_imgsz800 device="cpu"
```

### ... or using a python environment
```python
from ultralytics import YOLO
import os

# change the working directory so that the training results are saved to the correct folder.
os.chdir("path/to/yolov8/dataset/training_runs/")
# Load a pretrained model
model = YOLO("yolov8n.pt")

# train the model (transfer learning)
model.train(data="path/to/yolov8/boars.yaml",
            epochs=20,
            imgsz=800,
            batch=8,
            project = "path/to/yolov8/training_runs/",
            name="yolov8n_imgsz800",
            device="cpu")  # 0 for GPU (check pytorch installation hints) or "cpu"

```
- `model=yolov8n.pt`: Indicates the model to be used. Here, the YOLOv8 Nano model (`yolov8n.pt`) is used.
- `imgsz=800`: Determines the size of the input images in pixels. In this case, the image size is 800x800 pixels (default: 640).
- `data=path/to/boars.yaml`: Specifies the path to the data file that defines the training and validation data.
- `epochs=200`: Sets the number of training epochs. Here, it is 200 epochs.
- `batch=8`: Determines the batch size, i.e., the number of images processed simultaneously. Here, it is 8 (default 16).
- `project=/path/to/your/project/training_runs/`: Indicates the project directory where the training runs will be saved.
- `name=yolov8n_imgsz800`: Sets the name of the training run. This helps distinguish between different runs.
- `device="cpu"`: Specifies the CPU to be used for training. Alternatively, GPUs 0 and 1 can be used (device=(0,1)).

Check [here](https://docs.ultralytics.com/modes/train/#train-settings) for additional train settings and hyperparameters
### Example boars.yaml file

```yaml
# Contents inside the .yaml file

train: path\to\yolov8\train
val:   path\to\yolov8\valid
test:  path\to\yolov8\test

# total number of classes
nc: 2
names: ['boar','human']
```
## Predictions
### CLI
```bash
yolo predict model= .\training_runs\yolov8n_imgsz800\weights\best.pt source=.\test project=predictions name=yolov8n_imgsz800 conf=0.2 imgsz=800
```
### Python environment
```python
from ultralytics import YOLO
import cv2
from matplotlib import pylab as plt

# Load a trained model
model = YOLO("path/to/yolov8/training_runs/yolov8m_imgsz800/weights/best.pt")

# Use the model (predict on an image)    
results = model("path/to/yolov8/test",
                project = "path/to/yolov8/predictions",
                name = "yolov8m_imgsz800",
                show=True, 
                show_labels=False, 
                conf=0.2,
                imgsz=800,
                classes=None,
                save=True
                ) 

#%%     
# Plot the results (within matplotlib)
res_plotted = results[0].plot() # results[0]: show the first image
res_plotted_rgb=cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB) 
plt.imshow(res_plotted_rgb)

```
## Predictions (quantitative evaluation on independent images)

### The images must, of course, be labeled but should not have been used in training or validation.
```bash
yolo detect val model=path\to\weights\best.pt data=path\to\yourFile.yaml
```
## Tracking
```bash
yolo track model=path\to\weights\best.pt project=path\to\trackings\ name=yolov8n_800_botsort source="path\to\test\" tracker=botsort.yaml
```
[Here](https://github.com/phiflip/YOLOv8Lab/tree/main/scripts/Tracking) you can find the .yaml files for your tracker, as well as an additional script if you want to draw lines for your tracked paths.
