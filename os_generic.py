import os
print(os.getcwd())
os.chdir("/storage/emulated/0/Python program")
print(os.listdir(),'\n')
with open("notepad.py","r") as f:
	f1= f.read()
	print(f1)
os.replace("text2.txt","text.txt")
with open("text.txt","w") as f:
	f.write("Sunil")
f=open ("text.txt","r")
print(f.read())
f.close()