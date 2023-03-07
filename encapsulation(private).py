class encap:
    __a=10
    c=20
    def encapsulation(self):
        b=200
        print("private encapsulation:")
        print(self.__a+20)

obj=encap()

obj.encapsulation()
print(obj.__a)