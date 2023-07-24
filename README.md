# Atro-Keras-Security-Cam
Real-time Object and Person Detection using Pre-trained Keras Model
This program utilizes a pre-trained Keras model to classify real-time images from a webcam. It accurately identifies objects and people, providing confidence scores for the results. Designed with security purposes in mind, it proves particularly useful in settings such as schools and offices.

<img src="https://github.com/ArjunPramod/Atro-Keras-Security-Cam/assets/118660983/0318e437-5877-4dfe-85f3-a87f2ea3634a" alt="image" width="500" height="256">

## Requirements
- Python 3
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Discord (for sending messages)
## Usage
- Open the terminal and navigate to the project directory.
- Run the program: python3 main.py
- Grant the program access to your webcam.
- The program will display the webcam output in a window.
- Press the Esc key to exit the program.
- The program will output the results and send a message to a Discord channel.
## Configuration
- Edit the labels.txt file to match the class names of the pre-trained model.
- Replace the keras_model.h5 file with your own pre-trained model.
- Modify the records.xlsx file to match the information of the individuals being detected.
