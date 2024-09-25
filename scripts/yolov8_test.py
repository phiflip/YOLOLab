from ultralytics import YOLO
import cv2
from matplotlib import pylab as plt


# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# results = model("//bfhfilerbe01.bfh.ch/ahp1/Desktop/ahp1.jfif")  # predict on an image


# Plot the results (openCV)
res_plotted = results[0].plot()
# cv2.imshow("result", res_plotted)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

# Plot the results (Matplotlib)
res_pltted_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB) 

plt.figure()
plt.imshow(res_pltted_rgb)
