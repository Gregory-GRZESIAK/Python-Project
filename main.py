import datetime
import time
from other_function import *
from main_function import *
from probability_function import *
import cv2
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.collections.face_collections import Subjects

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '67fd5b97-afbf-48f3-9e0a-c4e32aebff67'

# Initialization
compre_face: CompreFace = CompreFace(DOMAIN, PORT)
recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
face_collection: FaceCollection = recognition.get_face_collection()
subjects: Subjects = recognition.get_subjects()

# ----------------------------------------------------------------------------------------------------------------------
execution_time_before = time_now()
#-----------------------------------------------------------------------------------------------------------------------

# Open the camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Photo")
photo_is_good = True
ret, frame = cam.read()

# If the camera could not open
if not ret:
    print("failed to grab frame")
    photo_is_good = False


# If the camera has opened correctly
if photo_is_good:
    cv2.imshow("Photo", frame)
    ret, frame = cam.read()
    img_name = "Picture.jpg"

    # Take a photo
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

    # Close the camera
    cam.release()
    cv2.destroyAllWindows()

    # Calculate the information related to the new photo
    image_path: str = img_name
    answer: dict = recognition.recognize(image_path=image_path, options={
                        "limit": 0,
                        "det_prob_threshold": 0.8,
                        "prediction_count": 1,
                        "face_plugins": "calculator,age,gender,landmarks, mask",
                        "status": "true"
                    })

    # If no face has been detected
    if "code" in answer:
        print("No face is found in the given image")

    # Is a face has been detected
    else:
        print(answer)
        print("")
        print(sentence("The person is a " + calc_gender(answer), (
                " | Probability :" + str(calc_prob_gender(answer)) + "%")))

        print(sentence("The person is " + str(calc_age(answer)) + " years old", (
            " | Probability :{0}".format(str(calc_prob_age(answer)) + "%"))))

        print(sentence("The person " + calc_mask(answer), (
                " | Probability :" + str(calc_prob_mask(answer)) + "%")))

        print(sentence(calc_someone(answer), (
                " | Probability :" + str(calc_prob_someone(answer)) + "%")))
        print("")


# ----------------------------------------------------------------------------------------------------------------------
execution_time_after = time_now()
#-----------------------------------------------------------------------------------------------------------------------
if execution_time_before[0] == execution_time_after[0]:
    print("Execution time : ", round(execution_time_after[1] - execution_time_before[1], 4), "s")
elif execution_time_before[0] == execution_time_after[0] - 1:
    print("Execution time : ", round((1 - execution_time_before[1]) + execution_time_after[1], 4), "s")