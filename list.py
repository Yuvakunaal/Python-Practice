# List : It is ordered mutable collection of items. 
# We create list using [] (square braces)

# creating a list
a = [10,20,30]
print(type(a))

# Accessing items
print(a[0],a[-1])

# Modification
a[0] = 100
print(a)

# appending
a.append(111)
print(a)

# insert -> first attr = index, second attr = what we want to insert
a.insert(2,50)
print(a)

# extend : one attr = list type
b = ["a","b"]
a.extend(b)
print(a)
b = ["a","b"]
b.extend(a)
print(b)

print(a)

# remove :- one attr = existing element inside the list
a.remove(111)
print(a)

# pop :- one attr = deletes the index element and return it (default = '-1' index)
a.pop()
print(a)

b = a.pop(3)
print(a)
print(b)

# index :- one attr = element
print(a.index(20))

# delete element using pop
element = 50
ind = a.index(50)
b = a.pop(ind)
print(f"deleted = {b} at index = {ind}")
print(a)

# delete : using del keyword
del(a[1])
print(a)

# length of list (not last index)
print(len(a))

# Looping over list :-
l = [20,30,40,10]
for i in range(len(l)):
    print(l[i])
    
print()
for i in l:
    print(i)


# List comprehension (*****)
# print squares of first 5 natual numbers
a = [i**2 for i in range(1,6)]
print(a)

# print squares of first 5 odd natual numbers
a = [i**2 for i in range(1,6) if i%2!=0]
print(a)

# sort :-
a = [4,5,3,1,2]
a.sort() # Time complexity = O(n)
print(a)

# O(1) < O(logn) < O(nlogn) < O(n) < O(n**2) < O(n**n) < O(n!) 

a.sort(reverse=True)
print(a)

# sorted
c = [4,3,5,2]
b = sorted(c)
print(b)
print(c) # no change in c
print()

# sort and display original and sorted 
d = [4,3,5,2,6]
e = sorted(d) # Ascending
print(d)
print(e)
print()
d = [4,3,5,2,6]
e = sorted(d,reverse=True) # Descending
print(d)
print(e)

# copy list :-
a = [1,2,3]
b = a.copy()
print(b)

# joining lists :-
c = a+b
print(c)

# finding min and max elements
print(min(d))
print(max(d))

# finding sum :-
print(f"sum = {sum(a)}")

# 2-d 
a = [[1,2],
     [3,4],
     [5,6]]
print(a[1][1])

# looping over 2-d list
print()

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j])
        
print()
# minimum element without using 'min'
a = [4,1,3,5]
b = sorted(a)[0]
print(f"min = {b}")

# maximum element without using 'max'
a = [4,1,3,5]
b = sorted(a)[-1]
print(f"max = {b}")