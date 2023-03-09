class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.stack1 = []
        self.stack2 = []
        
    def push(self, num):
        if num % 2 == 0:
            if len(self.stack1) < self.size:
                self.stack1.append(num)
            else:
                print("Stack 1 is full.")
        else:
            if len(self.stack2) < self.size:
                self.stack2.append(num)
            else:
                print("Stack 2 is full.")
    
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Both stacks are empty.")
            return None
        elif len(self.stack1) > 0:
            return self.stack1.pop()
        else:
            return self.stack2.pop()
    
    def display(self):
        print("Stack 1:", self.stack1)
        print("Stack 2:", self.stack2)
 
two_stacks=TwoStacks(5)

while True:
    print("Options:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Quit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        num = int(input("Enter number to push: "))
        two_stacks.push(num)
    elif choice == 2:
        num = two_stacks.pop()
        if num is not None:
            print("Popped number:", num)
    elif choice == 3:
        two_stacks.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
