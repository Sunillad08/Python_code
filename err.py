import matplotlib.pyplot  as plt
##from matplotlib.pyplot import style
plt.style.use("ggplot")
cases = [ 13564,24427 - 13564, 8903 ,8718,7639,4126,3986,3664,2173,2090,1914,1326,934,925,831,780,524,437,187,173,154,69,65,65,59,42,33,13,13,7,2,1,1,1]
state = ["mumbai","Maharashtra","Gujarat","Tamil Nadu","Delhi","Rajasthan","Madhya Pradesh","Uttar Pradesh","West Bengal","Andhra Pradesh","Punjab","Telangana","Jammu and Kashmir","Karnataka","Bihar","Haryana","Kerala","Odisha","Chandigarh","Jharkhand","Tripura","Uttarakhand","Assam","Himachal Pradesh","Chhattisgarh","Ladakh","Andaman and Nicobar Islands","Meghalaya","Puducherry","Goa" ,"Manipur","Arunachal Pradesh","Mizoram","Nagaland"]
mumbai, india = plt.subplots()
explo = []
for _ in range (34):
    explo.append(0)
india.pie( cases, labels=state , startangle=90 , explode = explo )
##, labels=state , startangle=90
##india.axis('equal')

#mumbai.pie
plt.show()
#print (len(cases),len(state))
