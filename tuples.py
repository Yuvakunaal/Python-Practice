# Tuples : immutable collection of items => '()'

t = (1,2,3,4)

# Accessing 
print(t[1])
print(t[-1])

# update
newt = t+(5,6)
print(t)
print(newt)

# unpack
a,b,c = (1,2,3)
print(a)
print(b)
print(c)

print()
# Looping over tuples :-
for i in t:
    print(i)    

# joining the tuples :-
T = t + newt
print(T)

# converting datatype to tuple
a = tuple([1,2,3])
print(a)

# Tuple methods :-
print(T.count(1))
print(T.index(5))