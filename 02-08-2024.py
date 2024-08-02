# Loops :-
# Two types :- while, for
# while loop :-
# 'while' keyword with condition -> increment or decrement based on condition

i = 1
while i<=5:
    print(i,end=" ")
    i+=1
print()
# end="", to keep printing in same line

i = 5
while i>=1:
    print(i,end=" ")
    i-=1
print()

# Display all even numbers from 1 to 10 (10 also included)
i = 1
while i<=10:
    if i%2==0:
        print(f"{i}",end=" ")
    i+=1
print()

# display [1,2,3,4,5,6,7] = [mon,tue,.....]
# if.. if.. -> first if true or false it will check second if
# if.. elif...  -> first if is false then only it will check elif
i = 1
while i<=7:
    if i==1:
        print(f"Monday")
    elif i==2:
        print(f"Tuesday")
    elif i==3:
        print(f"Wednesday")
    elif i==4:
        print(f"Thursday")
    elif i==5:
        print(f"Friday")
    elif i==6:
        print("Saturday")
    else:
        print("Sunday")
    i+=1

# for loop :-
# 'for' keyword with range or items -> ranging

# range(a,b,c) -> a=starting value(default=0), b=end value(will not considered), c=step(default=1)
for i in range(5):
    print(i+1)
    
print("----------")
# print even numbers from 0 to 10 using for
for i in range(0,11,2):
    print(i)

print("----------")
# print odd numbers from 0 to 10 using for
for i in range(1,10,2):
    print(i)

print("----------")
# print 5 table till 50 value
for i in range(0,11):
    print(f"5 x {i} = {5*i}")
    
# Ask user to input a number and print natural numbers till the user inputted number
num = int(input("Enter number : "))
for i in range(1,num+1):
    print(i)

# check whether the number is palindrome or not
# 121 = 121 -> palindrome, 123 != 321 -> not palindrome

# 123 -> 3, 0*10=0, 0+3 = 3,...12
# 12 -> 2, 3*10=30, 30+2 = 32,...1       
# 1 -> 1, 32*10=320, 320+1 = 321,...0
# rev=321
num = int(input("Enter number : "))
num1 = num
rev = 0

while num>0:
    a = num%10
    rev = (rev*10)+a
    num //= 10

if num1 == rev:
    print(f"{num1} is palindrome")
else:
    print(f"{num1} is not a palindrome")

# Find factorial of a number
# 5 -> 5! = 5*4*3*2*1 = 120
a = 1
num = int(input("Enter number : "))
for i in range(1,num+1):
    a *= i
print(a)

# *
# **
# ***
# ****
# *****
num = 5
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()
    
print("----------")
# *****
# ****
# ***
# **
# *
num = 5
for i in range(0,5):
    for j in range(i,5):
        print("*",end="")
    print()

print("----------")
# *****
# *****
# *****
# *****
# *****
num = 5
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()

