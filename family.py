import os

class lad_member:
	def __init__(self,name,age,blood_group):
		self.name = name
		self.last = "Lad"
		self.age = age
		self.blood_group = blood_group
Sunil = lad_member("name",18,"A+")
Gauri = lad_member("Gauri",14,"B+")
Chandrakant = lad_member("Chandrakant",43,"A+")
name_list = [Sunil,Gauri, Chandrakant]
for i in name_list:
	name = i
	print(name.name,name.last,name.age,name.blood_group) 
print(os.getcwd())
