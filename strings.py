# 04-08-2024

# Strings continuation

# Mutable = which can be changed, immutable = which cannot be changed
# Strings are immutable

# Modifying the string
a = "hi"
a = "hello"
print(a)

# Concatenation : joining string2 to string1 (+)

a = "Yuva"
b = "Satya"
c = a+" "+b
print(c)

d = c+" "+"kunaal"
print(d)

# String formatting
name = "kunaal"
age = 19
a = "I am {}, my age is {}".format(name,age)
print(a)

# excape characters
a = "This is \"kunaal\""
print(a)

a = "This is kunaal \ncbit"
print(a)

a = "This is yuva\tkunaal"
print(a)

a = "for i in range(2):\n\tprint(i)"
print(a)

# String methods :-
# uppercase,lowercase,strip,replace,split

a = "HeLlo"
b = a.upper()
print(b)

c = a.lower()
print(c)
a = "  hello  "
print(a)
a = a.strip()
print(a)

# every professional will use strip for every userinput
a = input("Enter number : ").strip()
print(a[1])

a = "Kunaal mgit"
a = a.replace("mgit","cbit") # str.replace(where-to-replace,what-to-replace)
print(a)

# split
a = "hello cbit 31 kunaal"
b = a.split(" ")
print(b)

a = "I am cbitian,I am pythonian,I am meghanaian"
b = a.split(",")
print(b)

a = input("enter name : ").strip()
b = a.split(" ")
print(b)

name = "kunaal"
a = len(name)
print(a)

# Problems :-
# Python code to get a string made of first 2 and last 2 characters from given string
# string = "kunaal", newstring = "kual"
main = "kunaal"
ans1 = f"{main[:2]}{main[-2:]}"
print(ans1)
# or
main = "kunaal"
ans2 = main[:2] + main[-2:]
print(ans2)

# String iterating :-
name = "kunaal"
for i in name:
    if i in "aeiou":
        print(i)

# Problems :-
# count the no of vowels and consonants
v = 0
c = 0
string = "smartinterview"
for i in string:
    if i in "aeiou":
        v+=1
    else:
        c+=1
print(f"Vowel count = {v}\nConsonant count = {c}")

v = 0
c = 0
string = "smartmeghs"
for i in range(len(string)):
    if string[i] in "aeiou":
        v+=1
    else:
        c+=1
print(f"Vowel count = {v}\nConsonant count = {c}")



