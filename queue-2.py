import queue

L=queue.Queue(maxsize=5)
L.put(input("enter the value:"))
L.put(input("enter the value:"))
print(type(L))
print(L.get())
print(L.get())