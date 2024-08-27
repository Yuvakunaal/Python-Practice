import math as m

# checking functions there in math :-
# for i in dir(math):
#     print(i)
# print(dir(math))

# math module
def mathmodules():
    print(m.factorial(5))
    print(m.sqrt(121))
    print(m.pow(2,4)) # 2**4
    print(m.floor(2.7)) # decimal before + 0
    print(m.ceil(2.3)) # decimal before + 1
    print(m.log(2))
    print(m.gcd(9,10))
    print(m.isfinite(1222))
    print(m.inf)
    print(m.isfinite(m.inf))
    print(m.e)
    print(m.pi)
    print(len(dir(m)))
# mathmodules()

# from math import *
# print(factorial(3))
# print(sqrt(16))
# print()

# datetime module
from datetime import datetime,date
def datetimes():
    # a = datetime.today()
    a = date.today()
    print(a)
    print(a.weekday()) # 0 = monday, 6 = sunday

    print()

    b = date(2005,2,24)
    print(b)
    print(b.weekday())
    print(b.isoweekday()) # 1 = monday, 7 = sunday
# datetimes()


# random module
import random
def randoming():
    a = random.random() # 0 - 1 => value range
    b = random.randrange(1,10) # step = default : 1
    c = random.randint(1,10)

    option = ["Rock","Paper","Scissor"]
    d = random.choice(option)
    print(a)
    print(b)
    print(c)
    print(d)
# randoming()

