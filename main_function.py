from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.collections.face_collections import Subjects

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '67fd5b97-afbf-48f3-9e0a-c4e32aebff67'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

subjects: Subjects = recognition.get_subjects()


# The different functions below will simply look for the information obtained in "answer"
#-----------------------------------------------------------------------------------------------------------------------
def calc_gender(answer):
    result = answer["result"]
    result_part_2 = result[0]
    gender = result_part_2["gender"]
    gender_result = gender["value"]
    return gender_result



def calc_age(answer):
    result = answer["result"]
    result_part_2 = result[0]
    age = result_part_2["age"]
    age_result_high: int = age["high"]
    age_result_low: int = age["low"]
    return int((age_result_high + age_result_low)/2)



def calc_mask(answer):
    result = answer["result"]
    result_part_2 = result[0]
    mask = result_part_2["mask"]
    mask_result = mask["value"]
    if mask_result == "without_mask":
        return "has no mask"
    elif mask_result == "mask_worn_incorrectly":
        return "put on his mask badly"
    else:
        return "correctly put on his mask"



def calc_someone(answer):
    result = answer["result"]
    result_part_2 = result[0]
    someone = result_part_2["subjects"]
    if not someone:
        return "We did not find who owned this face"
    else:
        someone_part_2 = someone[0]
        someone_result = someone_part_2["subject"]
        return str("The person is" + someone_result)
