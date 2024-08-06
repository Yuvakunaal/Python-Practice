# 04-8-2024, 06-08-2024

# Functions :-
# Function defination, Function calling

def myfunc():
    print("My first function !")

# myfunc()

def even():
    a = 2
    if a%2==0:
        print(True)
    else:
        print(False)
# even()

# return keyword : stop function execution at that line and returns which we give

def odd():
    a = 3
    if a%2!=0:
        return True
    return False
# a = odd()
# print(a)

def is_odd(num): # num -> parameter (which we receive when function is called) i.e.., num = 5
    if num%2!=0:
        return True,1
    return False,0

# i = 2
# a,b = is_odd(i) # argument passing
# print(a,b)

# multiple arguments
def f1(a,b,c):
    return a+b+c
a = f1(1,2,3)
print(a)

# default arguments
def is_odd(num="not given"): # num -> parameter (which we receive when function is called) i.e.., num = 5
    if num=="not given":
        return "You didnt passed argument"
    if num%2!=0:
        return True
    return False
a = is_odd(4)
print(a)

# keyword arguments
def f2(a,b,c):
    return a,b,c
a = f2(b=2,a=1,c=3)
print(a)