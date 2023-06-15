import cv2
from deepface import DeepFace
import time

start_time=time.time()
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



while True:
    info={
    "Emotion":[],
    "Age":[],
    "Gender":[],
    "Race":[]
    }

    ret, frame = camera.read()
    cv2.imshow("frame", frame)


    _, start_frame=camera.read()      
    inspect = DeepFace.analyze(start_frame, actions=("gender","age","race","emotion"))
    info["Age"].append(inspect[0]["age"])
    info["Emotion"].append(inspect[0]["dominant_emotion"])
    info["Gender"].append(inspect[0]["dominant_gender"])
    info["Race"].append(inspect[0]["dominant_race"])
    print(info)
    time.sleep(30.0) # The script re-downloads the actions of gender, age, race, and emotion every 30 seconds. 
    if cv2.waitKey(1) == ord('q'):
        break
  
camera.release()
cv2.destroyAllWindows()
