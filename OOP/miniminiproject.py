# Create a calculator
# +,-,*,/,%

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        print(f"Sum = {self.num1+self.num2}")
    
    def subtract(self):
        print(f"Difference = {self.num1-self.num2}")
    
    def multiplication(self):
        print(f"Product = {self.num1*self.num2}")
    
    def division(self):
        print(f"Division = {self.num1/self.num2}")
    
    def remainder(self):
        print(f"Remainder = {self.num1%self.num2}")

calc = Calculator(3,2)
calc.addition()
calc.remainder()
calc.subtract()
calc.multiplication()
calc.division()
