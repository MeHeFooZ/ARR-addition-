class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
        
obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.display()
print("\n")
obj.insert_start(111)
obj.display()            