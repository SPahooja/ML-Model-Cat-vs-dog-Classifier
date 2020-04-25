import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

TrainingData = r"C:\Users\pahoo\OneDrive\Desktop\Classifier(Cat vs Dog)\PetImages/"

Categories = ["Dog", "Cat"]

for animal in Categories:
    DataPath = os.path.join(TrainingData,animal)
    for image in os.listdir(DataPath):
        img_array = cv2.imread(os.path.join(DataPath,image),cv2.IMREAD_GRAYSCALE) #can remove grayscale,but will be slow
        plt.imshow(img_array,cmap='gray')
        plt.show()
        break
    break

img_size = 100

img_array = cv2.resize(img_array,(img_size,img_size))

    

