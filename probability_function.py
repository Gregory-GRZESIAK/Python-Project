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
def calc_prob_gender(answer):
    result = answer["result"]
    result_part_2 = result[0]
    gender_prob = result_part_2["gender"]
    gender_prob_result = gender_prob["probability"]
    gender_prob_result = gender_prob_result*100
    if gender_prob_result == 100:
        return gender_prob_result
    else:
        return round(gender_prob_result, 2)



def calc_prob_age(answer):
    result = answer["result"]
    result_part_2 = result[0]
    age_prob = result_part_2["age"]
    age_prob_result = age_prob["probability"]
    age_prob_result = age_prob_result*100
    if age_prob_result == 100:
        return age_prob_result
    else:
        return round(age_prob_result, 2)



def calc_prob_mask(answer):
    result = answer["result"]
    result_part_2 = result[0]
    mask_prob = result_part_2["mask"]
    mask_prob_result = mask_prob["probability"]
    mask_prob_result = mask_prob_result*100
    if mask_prob_result == 100:
        return mask_prob_result
    else:
        return round(mask_prob_result, 2)



def calc_prob_someone(answer):
    result = answer["result"]
    result_part_2 = result[0]
    someone_prob = result_part_2["subjects"]
    if not someone_prob:
        return "100"
    else:
        someone_prob_part_2 = someone_prob[0]
        someone_prob_result = someone_prob_part_2["similarity"]
        someone_prob_result = someone_prob_result*100
        if someone_prob_result == 100:
            return someone_prob_result
        else:
            return round(someone_prob_result, 2)
