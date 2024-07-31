# Comments
'''
# Variable :-
a = 1
_ = 2
# no number variable

# ---------
# Displaying or printing
# type-1
print(a,"=","hello\nhi")
print("😂")
# ',' = sameline + single space

# type-2
print(f"{a} = hello")

# nextline : '\n'

# ---------
# Datatypes :-
# 1. Numbers - int,float,complex : a+jb = 2+2j ,boolean
# 2. Strings - str ('' , "")
# 3. list = list = [..]
# 4. tuple = tuple = (..)
# 5. dictionary = dict = {"a":1,...}
# 6. set = set = {1,2...}

# int
a = -10
print(f"{a}")
a = 10
print(f"{a}")
b = type(a)
print(f"{b}")

# float
a = 1.1
print(a)
b = type(a)
print(b)

# complex
a = 2+2j
print(a)
print(type(a))

# boolean : 0,null,None,empty = False, ... = True
a = True
b = False
print(a)
print(b)
print(type(a))
print(type(b))

# String
a,b = "hello","hi"
print(a)
print(b)
print(f'{type(a)}\n{type(b)}')
'''

# -----------------
# type - convertion
# we use -> int(), float(), complex() , str() 
# float -> int
a = 1.9
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

# int -> float
a = 1
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))

# int -> complex
a = 2
print(a)
print(type(a))
b = complex(a)
print(b)
print(type(b))

# float -> complex
a = 2.3
print(a)
print(type(a))
b = complex(a)
print(b)
print(type(b))

# complex -> int : we cant do
# complex -> float : we cant do

# int -> str
a = 2
print(a)
print(type(a))
b = str(a)
print(b)
print(type(b))

# str -> int
a = "12"
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

# float -> str
a = 2.5
print(a)
print(type(a))
b = str(a)
print(b)
print(type(b))

# str -> float
a = "2.5"
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))

# int -> boolean 
a = 2
print(a)
print(type(a))
b = bool(a)
print(b)
print(type(b))

# boolean -> int
a = True
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))

# float -> boolean 
a = 0.5
print(a)
print(type(a))
b = bool(a)
print(b)
print(type(b))

# boolean -> float
a = True
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))

