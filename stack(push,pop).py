stack=[]
def push():
    element=int(input("enter the value:"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("Removed the element",e)
        print(stack)

while True:
    print("selet the operations \n1.push\n2.pop\n3.Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("ENTER THE CORRECT VALUE.")