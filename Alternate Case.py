s=input("Enter the String: ")
s2=""
count=0
for i in s:
    if(i!=" " and count%2==0):
        s2+=i.lower()
        count+=1
    elif(i!=" " and count%2!=0):
        s2+=i.upper()
        count+=1
    else:
        s2+=" "
print(s2)
        
        
    
           