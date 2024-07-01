a=int(input("enter the number:"))
rev=0
x=a
while(a>0):
    rev=(rev *10)+a%10
    a=a//10
if x==rev:
    print("yes,it is palindrome")
else:
    print("no,it is not palindrome")


