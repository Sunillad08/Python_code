import os
import random
print(os.getcwd())
os.chdir("/storage/emulated/0/Python program")
#print(os.listdir(os.getcwd()))
#os.replace("quotes.txt","quotes.py")
#print(os.listdir())
f=open("turtle3.py","r")
print (f.read())
f.close()

print(random.randint(1,10000))