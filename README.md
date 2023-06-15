# Live-Video-Attribute-Analysis
Utilizes a camera to display the predicted attributes about a human subject in view (age, race, gender, emotion) via the Python Library DeepFace.

Based off of the YouTube user NeuralNine's age and gender predictor for static images. 
NeuralNine Youtube Video: https://www.youtube.com/watch?v=hvNj7Js9RyA


This project combines that functionality with a video display provided by the cv2 library to detect the attributes of a human face in sight of the camera every 30 seconds.

Timeline

06/15/2023: The script functions as intended, however there are a few bugs impacting optimality:

-The video frame window that appears upon starting the script is almost always frozen and does not provide a sufficient video feed
-The script re-downloads the actions of age, race, gender, and emotion every 30 seconds as it is prompted to complete a scan
-The script crashes when no face is in view of the camera
