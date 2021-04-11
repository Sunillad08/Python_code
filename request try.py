import requests
#print(dir(requests))

n = requests.get("https://www.google.com/")
print(n.text)