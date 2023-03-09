queue=[]
def enqueue():
    element=int(input("enter the value:"))
    queue.append(element)
    print(element,"is added in q")

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("Removed the element",e)
def display():
    print(queue)

while True:
    print("selet the operations \n1.add\n2.remove\n3.show\n4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("ENTER THE CORRECT VALUE.")