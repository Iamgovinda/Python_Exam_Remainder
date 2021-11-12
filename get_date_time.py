from datetime import *
import time

def get_remaining_time():
    current_date_time = datetime.now()   #returns the current date time in time-delta function.
    preboard_date_time = datetime(2021, 11, 14, 7, 00, 00)
    remaining_time = preboard_date_time - current_date_time    #returns the remaining time.
    return f"Please read for preboard!!!\nRemaing time is {remaining_time}(hrs:min:sec)"

get_remaining_time()