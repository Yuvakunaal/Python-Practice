# map : It lets you apply a function to all items in the input list
# numbers = [1,2,3,4,5]
# square_of_numbers = list(map(lambda x:x*x,numbers))
# print(square_of_numbers)

# # taking multiple inputs in single line
# a = list(map(int,input("Enter : ").split(" ")))
# print(a)


# find sum of numbers
# i/p : 1st line no of test cases
# t = int(input("No of test cases : "))
# for i in range(t):
#     l = list(map(int,input("Enter numbers with spacing : ").split(" ")))
#     print(sum(l))


# Filter : filter items on input list based on a function that returns True or False

nums = [1,2,3,4,5,6]
# [2,4,6]
filtering_evens = list(filter(lambda x:x%2!=0,nums))
print(filtering_evens)

# reduce : Inputting list -> single value  
from functools import reduce
sonums = reduce(lambda x,y:x+y, nums)
print(sonums)