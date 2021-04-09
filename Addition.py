print("Enter exactly 3 Numbers")
x=int(input())
y=int(input())
z=int(input())
print(x , y, z)
def check(x,y,z):
  if (x==y and y==z):
     print("Three numbers are exactly same! Lazy bum")
     s=3*x
     return s
  elif  (x==y or y==z or z==x):
      print("Two numbers are same!can't you imagine one more number?")
      s=x+y+z
      return s
  else :
       s=x+y+z
       return s
z=check(x,y,z)
print(z)
print("wanna know how much is 7+8+9 is?")
c=check(7,8,9)
print(c)