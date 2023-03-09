from queue import LifoQueue

s=LifoQueue(maxsize=3)

print(s.qsize())

s.put(input("enter the value:"))
s.put(input("enter the value:"))
s.put(input("enter the value:"))
  
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())