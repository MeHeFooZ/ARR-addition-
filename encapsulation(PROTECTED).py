class encap:
    _a=10
    c=20
    def encapfunction(self):
        b=200
        print("the encapsulation")
        print(self._a+50)

obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

