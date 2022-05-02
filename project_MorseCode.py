################################################
# File:    project_MorseCode.py
# Author:  Y. Ukawa
# Date:    Apr 14, 2022
# Project: Morse Code
################################################


MORSE_CODE_DICT = {
    'A':'.-',    'B':'-...',  'C':'-.-.',  'D':'-..',   'E':'.',
    'F':'..-.',  'G':'--.',   'H':'....',  'I':'..',    'J':'.---',
    'K':'-.-',   'L':'.-..',  'M':'--',    'N':'-.',    'O':'---',
    'P':'.--.',  'Q':'--.-',  'R':'.-.',   'S':'...',   'T':'-',
    'U':'..-',   'V':'...-',  'W':'.--',   'X':'-..-',  'Y':'-.--',
    'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----',
    } 


def convert_mc(string):
    mc = ''
    for l in string:
        try:
            mc += MORSE_CODE_DICT[l]
        except:
            continue
    # print(mc)
    return mc

def  test_palindrome(string):
    print("\nMorse Code Palindrome?")
    if string == '':
        print("NO")
        return
    if string == string[::-1]:
        print("YES")
    else:
        print("NO")



# Main
string = input("Enter a string:\n")
upper_str = string.upper()
mc = convert_mc(upper_str)
test_palindrome(mc)
