# Hand Gesture Recognition

### Introduction
In this project I have proposed a Hand Gesture Recognition system that can be used to operate the Kiosk Machine in a touch-less way. Self-service kiosk machines have gained a lot of popularity and they are used at many public places like a restaurant, movie theatres, malls, etc. A hand gesture recognition system can be used to prevent the physical contact between the users and the kiosk machine considering the effects Covid-19 pandemic had on the world.
The following block diagram shows the different components involved in the system :

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/Block%20Diagram.jpg" width=700/>
</p>

### CNN Model
After testing different models like VGG-16, ResNet-50, Inception, etc the Inception-ResNet v2 model gave the highest accuracy among all. The model is fine tuned by freezing its layers and adding custom layers on top. The input image size for this model is a coloured image of 75x75 pixels. The structure of the model is shown in the image below:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/Incepresnet%20layers.png" width=800 />
</p>

The model was trained for 15 epochs. Performance of the model was evaluated using different metrics such as accuracy, sensitivity, specificity, area under the ROC curve, and confusion matrix. Categorical cross-entropy was used as the loss function. Categorical cross-entropy is used along with the softmax function for classification since it’s a multi-modal classification containing 4 classes. The softmax function predicts the probabilities for each class meanwhile the categorical cross-entropy loss function measures the distance of those probabilities from the actual truth values of the classes. Mathematically the Categorical Cross-Entropy loss for this problem can be represented as follows:

<p aligh="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/CE_loss%20formula.png" width=300 /> 
</p>
 where the term y<sub>p</sub> gives the probability for positive class and the denominator term is used for normalizing the probalities of all the classes.
 
 ### Dataset
To train the CNN models, we prepared a dataset consisting of 4 hand gestures to perform 4 basic GUI operations in a kiosk machine namely “back”, “forward”, “submit” and “clear/cancel”. The dataset contains colored 75x75 sized images captured indoors, in public places, and outdoor surroundings under different lighting conditions. Fig 3 shows the 4 classes of hand gestures. The dataset contains 500 images per class for training and another 100 images as validation data. The validation data is captured mostly at places with bright natural or artificial lighting. Gestures and their respective actions are shown in the image below: 

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/gestures.jpg" width=800 />
</p>

### Results
Model was able to achieve an accuracy of 0.96 and 0.95 on the training and validation data respectively. Meanwhile the loss was 0.1 and 0.18 for training and validation data respectively. The graphs below show the variation of accuracy and loss over the 15 epochs for which the model was trained:

<p float="left">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/accuracy.png" width="500" />
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/loss.png" width="500" /> 
</p>

The following image shows the combined confusion matrix for the 4 classes:

<p align="center">
  <img src="https://github.com/Nikxiii/Hand-Gesture-Recognition/blob/main/Diagrams/confusion.png" width=500 />
</p>



