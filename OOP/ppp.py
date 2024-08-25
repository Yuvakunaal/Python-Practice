class Hello:
    def __init__(self,name,age,roll):
        self.name = name
        self._age = age
        self.__roll = roll
    def display(self):
        print(self.__roll)

obj = Hello("kunaal",190,31)
print(obj.name)
print(obj._age)
obj.display()
# print(obj.__roll) # u will get error