import random
import os

def getcor():
    en_x = random.randint(-400,400)
    en_y = random.randint( 100 , 300)
    return en_x , en_y
try:
    for i in range(80):
        print(getcor() , end = " + ")
        print(dir(random))
except Exception as e:
    print(e)
    
