# Real-time Webcam Security with Discord Intrusion Alerts

Enhance your security with this robust real-time webcam security system using pre-trained Keras models. Receive instant Discord alerts for detected intrusions, ensuring peace of mind in various settings, including schools and offices.

<img src="https://github.com/ArjunPramod/Atro-Keras-Security-Cam/assets/118660983/0318e437-5877-4dfe-85f3-a87f2ea3634a" alt="Webcam Security" width="500" height="256">

## Overview

This program leverages the power of pre-trained Keras models to classify real-time images from your webcam. It accurately identifies objects and people while providing confidence scores for each detection. Designed with security in mind, it offers a valuable layer of protection for your premises.

## Requirements

Before getting started, ensure you have the following dependencies installed:

- Python 3
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pandas
- Discord (for sending alerts)

## Usage

Follow these simple steps to use the system:

1. Open your terminal and navigate to the project directory.
2. Run the program: `python3 main.py`
3. Grant necessary permissions for accessing your webcam.
4. The program will display the webcam output in a dedicated window.
5. Press the `Esc` key to gracefully exit the program.
6. The program will output detection results and send an immediate alert to a specified Discord channel.

## Configuration

Customize the system to meet your specific requirements:

- Edit the `labels.txt` file to align class names with your pre-trained model.
- Replace the `keras_model.h5` file with your own trained model for tailored detection.
- Modify the `records.xlsx` file to manage information related to individuals being detected.

## Credits

This innovative security project was crafted by Arjun Pramod and is publicly available on [GitHub](https://github.com/ArjunPramod/Real-time-Webcam-Security-with-Discord-Intrusion-Alerts).

If you have questions or encounter any issues, please don't hesitate to [open an issue](https://github.com/ArjunPramod/Real-time-Webcam-Security-with-Discord-Intrusion-Alerts/issues).

**Experience enhanced security with real-time webcam monitoring and immediate Discord intrusion alerts!**
