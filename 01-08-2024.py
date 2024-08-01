# Operators :-
# 1. Arithmetic : + - * / % // **
# 2. Comparison : == != < > <= >=
# 3. Assignment : += , -=, *=, /=, //=, **=
# 4. Logical : and or not 
# 5. Bitwise : & | ^ ~ << >>
# 6. Membership : in, not in
# 7. Identity : is, is not

# 1. Arithmetic :-
a = 2
print(a+3+a) # 7
print(a-3) # -1
print(a*3) # 6
print(a/3) # 0.66..
print(a%3) # 2
print(a//3) # 0
print(a**3) # 8

# 2. Comparison :-
a = 2==3
print(a)
a = 2
print(a==2)
print(a!=2)
print(a<2)
print(a>2)
print(a<=2)
print(a>=2)

# 3. Assignment :-
a = 1
a += 1
print(a)

a = 1
a -= 1
print(a)

a = 1
a *= 1
print(a)

a = 1
a /= 1
print(a)

a = 1
a %= 1
print(a)

a = 1
a //= 1
print(a)

a = 1
a **= 1
print(a)

# 4. Logical :-
a = 2 and 2
print(a)

a = 0 or 0 or 1
print(a)

a = 0 or 0 and 1
print(a)

a = not 0
print(a)

a = not 0 or 1
print(a)

# 5. Bitwise : 1,0
a = 4
b = 1
c = 0
print(f"a & c = {a&c}")
print(f"a | c = {a|c}")
print(f"a ^ b ^ c = {a^b^c}") # XOR : only single '1' = True = 1
print(f"~ a = {~a}")
# 2's complement
# example : 1110 => 0001 => 0001+1 => 0010 => 0*2^3 + 0*2^2 + 1*2^1 + 0*2^0 => 2 (since before doing 2's complement the starting bit is 1, so number is considered as -ve) ==>> final answer = -2

print(f"a << b = {a<<b}") # a*(2**b) = 4*(2**3) = 32
print(f"a >> b = {a>>b}") # a//(2**b) = 4//(2**1) = 2 & = 4//(2**3) = 4 // 8 = 0

# 6. Membership :-
a = [2,3,4]
print(2 in a)
print(2 not in a)

# 7. Identity :-
a = 2.0
print(2 is a)
print(2 is not a)

# User input
a = int(input("Enter number : ")) # str -> int
print(a+5)

a = float(input("Enter number : ")) # str -> float
print(a)

a = str(input("Enter name : ")) # or input()
print(a)

a = bool(input("Enter anything : ")) # everytime true
print(a)

# Control flow :- (condition checkers)
# if, elif, else
# condition true -> 'if' body will execute

# if 
a = 2
if a == 2:
    print(f"{a} is equal to 2")
print("finished-1")

# if else
a = 3
if a == 2:
    print(f"equal to 2")
else:
    print(f"not equal to 2")
print("Finished-2")

# if elif else
a = 2
if a == 2:
    print(f"equal to 2")
elif a == 3:
    print(f"equal to 3")
else:
    print(f"not equal to 2 and also 3")
    
# Nested if
user = int(input("Enter number : "))
a = 1
b = 2
if user == a:
    if user == b:
        print(f"equal to {a} and also equal to {b}")
    else:
        print(f"equal to {a} but not equal to {b}")
else:
    print(f"its is not equal to {a} itself")

# if -> and or not
a = 1
b = 2
if a == 1 and b != 2:
    print(f"{a} = 1 and {b} = 2")
else:
    print(f"either a is not equal to 1 or b is not equal to 2, neither a is equal nor b is equal")

#----------------------------- 
if a==1 or b==2:
    print(f"{a} = 1 or {b} = 2")
else:
    print(f"both {a} = 1 and {b} = 2 are false")
    
#-----------------------------
if not a: 
    print("if")
else:
    print("else")

# Small example : Check whether the user-input is odd or even, if even display 'It is even', if odd display 'It is odd'
a = int(input("Enter number : "))
if a%2==0:
    print(f"It is even")
else:
    print(f"It is odd")
    
# Small example : check whether the user-input is leap year or not (%400==0, %100!=0 and %4==0, not leap)
year = int(input("Enter year : "))
if year%400 == 0:
    print(f"{year} is a leap year")
elif year%100 != 0 and year%4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

