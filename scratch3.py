# Import essential libraries
import requests
import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import cv2
import numpy as np
import imutils
import pickle
import tensorflow
from keras.models import load_model




framewidth = 300
framheight = 300
brightness = 100
threshold = 0.80
font = cv2.FONT_HERSHEY_SIMPLEX


cap=cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, framheight)
cap.set(10, brightness)

file = "keras_model.h5"
# load model
model = load_model('keras_model.h5')
pickle_in = open(file , "rb")
model = pickle.load(pickle_in)

def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img = cv2.equalizeHist(img)
    return img
def preProcessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

def getClassName(classNo):

    if   classNo == 0: return "Class 0"
    elif classNo == 1: return  "Class 1"
    elif classNo == 2: return " Class 2"


while True:

    success, imgOriginal = cap.read()

    img=np.asarray(imgOriginal)
    img = cv2.resize(img,(32,32))
    img = preProcessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1,32,32,1)

    cv2.putText(img, "CLASS: ", (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "PROBABILITY: ", (20, 75), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)

    #PREDICT IMAGE

    classIndex = int(model.predict_classes(img))
    predictions = model.predict(img)
    probabilityValue = np.amax(predictions)

    print(classIndex,probabilityValue)
    if probabilityValue > threshold:
        cv2.putText(imgOriginal, str(classIndex)+ " "+str(getClassName(classIndex)), (120,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(imgOriginal, str(round(probabilityValue*100, 2) )+"%", (180,75), font, 0.75, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow("Result", imgOriginal)

    classIndex = int(model.predict_classes(img))
    print(classIndex)
    print(classIndex)
    predictions = model.predict(img)
    probVal= np.amax(predictions)


    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()