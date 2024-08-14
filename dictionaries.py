# Dictionaries : Collection in which we have ordering, mutable indexed by keys (key - value pairs) '{}'

dic = {"a" : 1,"b" : 2}
print(dic)

# creating empty dict
b = dict()
print(b)

# Accessing 
print(dic["a"])
# or
print(dic.get("a"))

# Modify
dic["a"] = 10
print(dic)

# Add new item :-
dic["c"] = 200
print(dic)

# remove :-
dic.pop("b")
print(dic)
# or
dic["d"] = 300
print(dic)
del dic["c"]
print(dic)

# copy
dic1 = dic.copy()
print(dic1)

# remove all elements
dic.clear()
print(dic)

# Dictionary methods :-
a = dic1.keys()
print(a)

a = dic1.values()
print(a)

a = dic1.items()
print(a)

# Looping over dictionaries
# to access key
for key in dic1 :
    print(key)
    print(dic1[key])
print()

# to access both key and values
for key,value in dic1.items():
    print(key)
    print(value)
    
# Dictionary comprehension
d = {key : value*2 for key,value in dic1.items()}
print(d)