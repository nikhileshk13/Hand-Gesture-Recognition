# Hand Gesture Recognition

### Introduction
In this project, I have proposed a Hand Gesture Recognition system that can be used to operate the Kiosk Machine in a touchless way. Self-service kiosk machines have gained a lot of popularity and are used in many public places like restaurants, movie theatres, malls, etc. A hand gesture recognition system can be used to prevent physical contact between the users and the kiosk machine considering the effects the Covid-19 pandemic had on the world. The following block diagram shows the different components involved in the system :

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/Block%20Diagram.jpg" width=700/>
</p>

### Mediapipe-Hands Module
Mediapipe hands module is used here to obtain the bounding box for the hand. The image captured through the camera will be cropped to the size of the bounding box to remove the unnecessary part of the image before passing it as input to the CNN model. Apart from this, the landmark coordinates obtained from this module are used to control the mouse pointer and perform click action with the help of GUI automation tool- PyAutoGUI. As the coordinates of the index fingertip change when the hand is moved, the mouse pointer will be moved along those coordinates using PyAutoGUI functions. The following image shows the output from the Mediapipe-Hands module:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/mediapipe_landmarks.jpg"/ width=300>
</p>

References-

Mediapipe-Hands: https://google.github.io/mediapipe/solutions/hands.html

PyAutoGUI: https://pyautogui.readthedocs.io/en/latest/

### CNN Model
After testing different models like VGG-16, ResNet-50, Inception, etc the Inception-ResNet v2 model gave the highest accuracy among all. The model is fine-tuned by freezing its layers and adding custom layers on top. The input image size for this model is a colored image of 75x75 pixels. The structure of the model is shown in the image below:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/Incepresnet%20layers.png" width=800 />
</p>

The model was trained for 15 epochs. The performance of the model was evaluated using different metrics such as accuracy, sensitivity, specificity, area under the ROC curve, and confusion matrix. Categorical cross-entropy was used as the loss function. Categorical cross-entropy is used along with the softmax function for classification since it’s a multi-modal classification containing 4 classes. The softmax function predicts the probabilities for each class meanwhile the categorical cross-entropy loss function measures the distance of those probabilities from the actual truth values of the classes. Mathematically the Categorical Cross-Entropy loss for this problem can be represented as follows:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/CE_loss%20formula.png" width=300 /> 
</p>
 where the term y<sub>p</sub> gives the probability for the positive class and the denominator term is used for normalizing the probabilities of all the classes.
 
 ### Dataset
To train the CNN models, we prepared a dataset consisting of 4 hand gestures to perform 4 basic GUI operations in a kiosk machine namely “back”, “forward”, “submit” and “clear/cancel”. The dataset contains colored 75x75 sized images captured indoors, in public places, and in outdoor surroundings under different lighting conditions. Fig 3 shows the 4 classes of hand gestures. The dataset contains 500 images per class for training and another 100 images as validation data. The validation data is captured mostly at places with bright natural or artificial lighting. Gestures and their respective actions are shown in the image below:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/gestures.jpg" width=800 />
</p>

### Results
The model was able to achieve an accuracy of 0.96 and 0.95 on the training and validation data respectively. Meanwhile, the loss was 0.1 and 0.18 for training and validation data respectively. The graphs below show the variation of accuracy and loss over the 15 epochs for which the model was trained:

<p float="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/accuracy.png" width="400" />
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/loss.png" width="400" /> 
</p>

The following image shows the combined confusion matrix for the 4 classes:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/confusion.png" width=400 />
</p>



