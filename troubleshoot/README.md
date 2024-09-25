# yolov8lab Environment Troubleshooting

This directory outlines common issues with the **yolov8lab** environment. If you encounter issues where one tool stops working after installing the other, please follow the steps below to troubleshoot and resolve the problem.

---

### Problem Description

When installing **LabelImg** in the **yolov8lab** environment using **Conda**, **Spyder** no longer opens, and LabelImg does not launch either. However, uninstalling LabelImg restores Spyder’s functionality.

---

### Solution

#### Install LabelImg with `pip`

A simpler way to resolve the conflict between **Spyder** and **LabelImg** is to use **pip** to install **LabelImg**, as this method seems to bypass the package conflicts that occur when using Conda. 

Here’s the updated installation process:

1. First, ensure you are in the **yolov8lab** environment:

    ```bash
    conda activate yolov8lab
    ```

2. Install **LabelImg** using `pip`:

    ```bash
    pip install labelimg
    ```

This method has proven to resolve the issue without interfering with Spyder.

---

