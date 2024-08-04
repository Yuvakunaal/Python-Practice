# Strings
# Representation :-
# single quote, double quotes => (single line strings), multiline quotes => (multiline string)
a = 'hello world!'
b = "hello world"
c = '''
hello
welcome
to
cmr
cbit
'''
# print(f"{a}\n{b}\n{c}")


# Accessing using indexes
a = "hello"
print(a[2])
print(a[-1])


# Slicing :- string[a:b:c] -> a = start index(default=0), b = end index (but will not be considered in output)(default = last index + 1), c = step value (default = 1)
a = "Welcome"
print(a[3:7:1]) # a[3]+a[4]+a[5]+a[6]
print(a[2:]) # from 2nd index to end of string
print(a[:5]) # from start to 4th index of string
print(a[::2]) # alternative elements of string
print(a[::-1]) # start = 0,end = 7, [-1,-2,-3,-4,-5,-6,-7] = emocleW

# Reversing a string or int
# int -> string (becuase we can do slicing in strings)
# string -> int (after reversing)
a = 1234
b = int(str(a)[::-1])
print(b)
print(a==b) # check for palindrome
