
def fun_name(a,b,c):
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)

m=int(input("enter the value m:"))
n=int(input("enter the value n:"))
operator=input("enter the operator")
fun_name(m,n,operator)

