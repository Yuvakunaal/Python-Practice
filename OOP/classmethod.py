# class method : The method that are bound to the class and not the instance
# @ : indicated it is a decorator

class Student:
    name = "😂"
    @classmethod
    def display(cls):
        print(cls.name)

obj = Student()
obj.display()