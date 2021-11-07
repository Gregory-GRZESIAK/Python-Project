import datetime

def time_now():
    date = str(datetime.datetime.now())
    date_list = date.split(":")
    minutes = date_list[1]
    second = date_list[2]
    time = [minutes, round(float(second), 4)]

    return time



def sentence(start, end):
    len_start = len(start)
    space_number = 50 - len_start
    space = ""
    for i in range(space_number):
        space = space + " "

    sentence_final = start + space + end
    return sentence_final