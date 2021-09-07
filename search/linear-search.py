mylist=[3,7,9,8,6]

ele=7

flag=False
for i in mylist:
    if (i==ele):
        flag=True
        break
    
if (flag==True):
    print("Element found")
else:
    print("Element not found")