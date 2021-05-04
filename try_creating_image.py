import random

with open("test.photo" , "wb") as f:
    for i in range(100):
        f.write(random.randbytes(10))
    