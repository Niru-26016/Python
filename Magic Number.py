# You are required to write a Java program that determines whether a given positive 
# integer is a Magic Number. A number is called a Magic Number if the sum of its 
# digits is calculated repeatedly until a single-digit number is obtained, and that
# final single-digit value is 1. For example, the number 1729 is a magic number 
# because 1+7+2+9 = 19 → 1+9 = 10 → 1+0 = 1. Your task is to implement a program that
# accepts an integer as input, performs the repeated sum of digits, and prints whether 
# the number is a Magic Number or not. The program must also handle edge cases such as 
# single-digit inputs.

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
    



