############################################################
# File:    project_PotatoSacks.py
# Author:  Y. Ukawa
# Date:    Mar 24, 2022
# Purpose: Potato Sacks 
############################################################

def input_data():
    lk = []
    lc = []
    lsets = []
    p = int(input())
    for i in range(0, p):
        string = input()
        try:
            data = [int(x) for x in string.split(' ')]
        except:
            print("\nV\tError…… Try again!")
            return input_data()
        if len(data) != 12:
            print("\nV\tIncorrect length…… Try again!")
            return input_data()
        if not 10 <= data[1] <= 30:
            print("\nV\tOut of range…… Try again!")
            return input_data()
        for d in data[2:13]:
            if not 1 <= d <= 3:
                print("\nV\tOut of range…… Try again!")
                return input_data()

        lk.append(data[0])
        lc.append(data[1])
        lsets.append(data[2:11])
    return p, lk, lc, lsets

    
def calc_sacks(k, c, sets):
    print(k, end = " ")
    q, r, s = sets.count(1), sets.count(2), sets.count(3)
    for x in range(0, q + 1):
        for y in range(0, r + 1):
            for z in range(0, s + 1):
                if 1 * x + 2 * y + 3 * z == c:
                    print("YES")
                    return
    print("NO")
                    

# main

p, lk, lc, lsets = input_data()

for i in range(0, p):
    k, c , sets = lk[i], lc[i], lsets[i]
    calc_sacks(k, c, sets)

