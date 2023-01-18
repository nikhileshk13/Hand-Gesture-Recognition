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

Categorical cross-entropy was the loss function for this model. Categorical cross-entropy is used along with the softmax function for classification since it’s a multi modal classification containing 4 classes. The softmax function predicts the probabilities for each class meanwhile the categorical cross-entropy loss function measures the distance of those probabilities from the actual truth values of the classes. Mathematically the Categorical Cross-Entropy loss for this problem can be represented as follows:

