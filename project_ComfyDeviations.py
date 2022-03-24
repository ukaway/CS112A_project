############################################################
# File:    project_ComfyDeviations.py
# Author:  Y. Ukawa
# Date:    Mar 23, 2022
# Purpose: Evaluate 10 temperature values
#          by using the standard deviation
############################################################

import math


# ---------- convert input string to a float list ----------
def str_float():
    string = input()
    
    # check if there is a typo
    try:
        data = [float(x) for x in string.split(' ')]
    except:
        print("\nV\tError…… Try again!")
        return str_float()
    
    # check if each value is in the range 68-80
    for t in data:
        if not 68 <= t <= 80:
            print("\nV\tOut of range…… Try again!")
            return str_float()
        
    return data


# -------- get standard deviation from list values ---------
def calc_sd(data):
    sig = 0
    n = len(data)   
    if n < 2:
        return None
    mean = sum(data) / n
    for t in data:
        sig += (t - mean) ** 2
    sd = math.sqrt( sig / (n - 1))
    return sd


# ---------------- determine if comfy or not ---------------
def eval_sd(sd):
    print("\nResult:", end = ' ')
    if sd <= 1.0:
        print("COMFY")
    else:
        print("NOT COMFY")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~
print("V\tEnter 10 space separated temperature values")
print("V\tEach value will be in the range 68-80")

values = str_float()
sd = calc_sd(values)
eval_sd(sd)
# ~~~~~~~~~~~~~~~~~~~~~~~~ END MAIN ~~~~~~~~~~~~~~~~~~~~~~~~
