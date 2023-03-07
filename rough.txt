class vehicle:
    name=input('enter car name:')
    milage=input('enter milage of the car:') 
    cost=input("enter the cost :")
    model=input('enter the model:')

    def __init__(self):
        print("object created")

    def print_details(self):
        print(f"the name of the car is {self.name}\nAnd the cost is {self.cost}\nModel number is {self.model}\nthe milage we get in this {self.name} is approx of {self.milage}")
ob1=vehicle()
print("name=",ob1.name)
print("milage=",ob1.milage)
print("cost=",ob1.cost)
print("model=",ob1.model)

ob1.print_details()