# Inheritance : Inheritance is when a new class (called a child class or derived class) is created from an existing class (called a parent class or base class). The child class inherits all the attributes (variables) and methods (functions) of the parent class, but it can also have its own additional attributes and methods.


# single inheritance :-
class Parent:
    def __init__(self,hair):
        self.hair = hair
    def show(self):
        pass

class Child(Parent):
    def show(self):
        print(self.hair)

obj = Child("bald")
# obj.show()


# Multilevel inheritance :-
class Student1:
    def s1(self):
        print("student-1")

class Student2(Student1):
    def s2(self):
        print("student-2")
        
class Student3(Student2):
    def s3(self):
        print("student-3")
'''
obj1 = Student1() # s1
obj1.s1()
# obj1.s2() # error
# obj1.s3() # error

print()
obj2 = Student2() #s1,s2
obj2.s2()
obj2.s1()
# obj2.s3() # error

print()
obj3 = Student3()
obj3.s3()
obj3.s2()
obj3.s1()
'''

# Heirarchical inheritance :-
class College:
    def show(self):
        print("-CMR-")

class CSE(College):
    def show1(self):
        print("CSE")

class CSD(College):
    def show2(self):
        print("CSD")

class ECE(College):
    def show3(self):
        print("ECE")
'''
obj = College()
obj.show()
# obj.show1() # error
# obj.show2() # error
# obj.show3() # error

print()
obj1 = CSE()
obj1.show1()
obj1.show()
# obj1.show2() # error
# obj1.show3() # error

print()
obj2 = CSD()
obj2.show2()
obj2.show()
# obj2.show1() # error
# obj2.show3() # error

print()
obj3 = ECE()
obj3.show3()
obj3.show()
# obj3.show1() # error
# obj3.show2() # error
'''


# Multiple Inheritance :-
class Father:
    def show1(self):
        print("Father properties")
        
class Mother:
    def show2(self):
        print("Mother properties")
        
class Child(Father,Mother):
    def show3(self):
        print("Child properties")
'''
obj1 = Father()
obj1.show1()
# obj1.show2() # error
# obj1.show3() # error

print()
obj2 = Mother()
obj2.show2()
# obj2.show1() # error
# obj2.show3() # error

print()
obj3 = Child()
obj3.show3()
obj3.show1()
obj3.show2()
'''

# Hybrid inheritance
class Person:
    def show1(self):
        print("Person")
        
class Patient(Person):
    def show2(self):
        print("only Patient")

class Doctor(Person):
    def show3(self):
        print("Only Doctor")

class ResidentDoctor(Patient,Doctor):
    def show4(self):
        print("Resident Doctor")

obj1 = Person()
obj1.show1()
# obj1.show2() # error
# obj1.show3() # error
# obj1.show4() # error

print()
obj2 = Patient()
obj2.show2() 
obj2.show1()
# obj2.show3() # error
# obj2.show4() # error

print()
obj3 = Doctor()
obj3.show3() 
obj3.show1()
# obj3.show2() # error
# obj3.show4() # error

print()
obj4 = ResidentDoctor()
obj4.show3() 
obj4.show2() 
obj4.show4() 
obj4.show1()