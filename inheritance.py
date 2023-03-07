class vechile:
    name=input("enter the name of car:")
    def method_1(self):
        print("this is of method A beautiful car.")

class child(vechile):
    pass

ob=child()
print(ob.name)
ob.method_1()