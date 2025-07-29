"""Write a Java program that reads a sentence from the user and returns a new string in which the alphabetic characters alternate in case, starting with lowercase for the first letter. The alternation should apply only to letters, while non-letter characters such as spaces, digits, and punctuation marks should remain unchanged and should not affect the alternating pattern. For example, if the input is "Hello World!", the output should be "hElLo wOrLd!". Similarly, for the input "Java is fun!", the output should be "jAvA iS fUn!". The program should correctly handle both uppercase and lowercase letters and preserve the original spacing and punctuation."""

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
        
        
    
           