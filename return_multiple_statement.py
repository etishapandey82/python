#return multiple statement
'''def calculator(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add, sub ,mul, div
tup=calculator(10,20)
for i in tup:
    print(i,end=" ")'''


def calculator(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
    p,q,r,s=calculator(20,10)
    print("addition is",p)
    print("subtraction is",q)
    print("multiply is",r)
    print("division is",s)