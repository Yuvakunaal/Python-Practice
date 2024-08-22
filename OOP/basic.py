# class -> self keyword 

class Dog:
    def __init__(self):
        self.name = "harry potter"
    def display(self):
        print(self.name)

# animal = Dog()
# animal.display()


class Student:
    def __init__(self,name,roll,clg):
        self.name = name
        self.roll = roll
        self.clg = clg
    def show(self):
        print(f"Name = {self.name}, Roll = {self.roll}, Colege = {self.clg}")

# student = Student("Kunaal",31,"CBIT")
# student.show()

class Student:
    def __init__(self,name,roll,clg):
        self.name = name
        self.roll = roll
        self.clg = clg
    def show(self):
        return self.name,self.roll,self.clg

# student = Student("Kunaal",31,"Cbit")
# print(student.show())

class Operation:
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2
    def add(self):
        return self.n1 + self.n2
    
a = Operation(31,24)
print(a.add())
