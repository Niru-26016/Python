s=input("Enter The String: ")
s+=" "
s2=""
l_num=[]
l_alpha=[]
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        l_alpha.append(s[i])
        l_num.append(count)
        count=1
for i in range (len(l_num)):
    s2+=l_alpha[i]+str(l_num[i])
print(s2)