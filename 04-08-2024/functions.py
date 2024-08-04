# # functions :-(def keyword)
# def name():  # function defining
#     return 12
# a = name() # function calling
# print(a)


# # even code
# def evennumber():
#     a = int(input("Enter number : "))
#     if a%2 == 0:
#         return "even"
#     return "not even"

# a = evennumber()
# print(a)

def evennumber():
    a = int(input("Enter number : "))
    if a%2 == 0:
        return "even"
    return "not even"

def run1():
    a = evennumber()
    print(a)

def oddnumber():
    a = int(input("Enter number : "))
    if a%2 != 0:
        return "odd"
    return "not odd"

def run2():
    a = oddnumber()
    print(a)
    
run1()
run2()





