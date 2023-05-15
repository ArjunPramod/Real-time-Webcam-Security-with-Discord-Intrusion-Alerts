from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import pandas as pd
from statistics import mode
import discord
import time

from discord_msg import send_message
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

x = 0
List = []

# Load the model
try:
    model = load_model("keras_model.h5", compile=False)
except:
    print("Error loading model. Check that the file path is correct.")
    exit()

# Load the labels
try:
    with open("./labels.txt", "r") as f:
        class_names = [line.strip() for line in f]
except:
    print("Error loading labels. Check that the file path is correct.")
    exit()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Check if the camera is working
    if not ret:
        print("Error: Webcam not working")
        break

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the model's input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predict the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    List.append(class_name)

    # Print prediction and confidence score
    # print("Class:", class_name, end=" ")
    # print("Confidence Score:", str(np.round(confidence_score * 100)) + "%")

    ID = class_name
    SC = confidence_score * 100

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)
    print("Confidance: ", SC)

    x = x + 1
    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break


df = pd.read_excel('records.xlsx')

intr = 0
print(ID[2:], "\n")
# print(df.head(3))
# print(SC)
# print(df.loc[1])
for i in range(len(df)):
    if df.iloc[i][0] == ID[2:]:
        if SC > 60:
            print("Student ID: ", df.iloc[i][0][2:])
            print("Name: ", df.iloc[i][1])
            print("Lab: ", df.iloc[i][2])
            print("Role: ", df.iloc[i][3])
            print("Discord ID: ", df.iloc[i][4])
            break
        else:
            print('Intruder')
            break


camera.release()
cv2.destroyAllWindows()
time.sleep(2)
send_message(df.iloc[i][4])
