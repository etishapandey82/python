

a=int(input("enter the  first number:"))
x=int(input("enter the secon3d number"))
b=int(input("1-> Add, 2->sub,3->mul,4->div:"))
if b==1:
    print("addition of number is",a+x)
elif b==2:
    print("subtraction of two number is",a-x)
elif b==3:
    print("multiply of two number is ",a*x)
elif b==4:
    print("division of two number is",a/x)
else:
    print("invalid input")
