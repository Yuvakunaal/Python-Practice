# static method : That do not receive an implicit first argument, We dont need object creation.

class Hello:
    @staticmethod
    def add(x,y):
        return x+y
    
print(Hello.add(2,3))
