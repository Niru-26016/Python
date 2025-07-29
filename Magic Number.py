num=input("enter the number: ")
sum=0
while(len(num)>1):
    for i in num:
        sum+=int(i)
    num=str(sum)
    sum=0

if int(num) == 1:
    print("Magic number")
else:
    print("Not a Magic Number") 
    



