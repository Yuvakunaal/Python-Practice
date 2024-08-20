# Write a python code to find the factorial of a number :-
# 3 = 1*2*3
def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
# a = factorial(4)
# print(a)

# Write a python code to find first 'n' fibonacii numbers :-
# n = 5, 0 1 1 2 3
def fibo(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(c,end=" ")
# fibo(10)

# Write a python code to count no.of vowels and consonants in a string
def count_v_c(s):
    s = s.lower()
    v = 0
    c = 0
    for i in s:
        if i in "aeiou":
            v+=1
        else:
            c+=1
    return v,c
# vowels, consonants = count_v_c("kunaalmEgh")
# print(f"Count of Vowels = {vowels}, Count of Consonants = {consonants}")

# Write a python code to check whether the string is palindrome or not
# abcddcba = 0 1 2 3 -4 -3 -2 -1
def is_pali(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return "Not Palindrome"
    return "Palindrome"
# ans = is_pali("malayllam")
# print(ans)


# Write a python code to check whether two strings are anagrams or not
# s1 = "cat", s2 = "tac" -> anagram
def is_anag(s1,s2):
    if len(s1) != len(s2):
        return "Not Anagram"
    s11 = list(s1)
    s11.sort()
    s22 = list(s2)
    s22.sort()
    if s11 == s22:
        return "Anagram"
    return "Not Anagram"
# a = is_anag("cat","tac")
# print(a)


# Python code to find the sublist sum to zero,
# Ex : [1,2,-3,4,2,-6,7] => o/p : [1,2,-3],..
def sublist(l):
    dummy = []
    length = len(l)
    for i in range(length):
        for j in range(i,length):
            sub = l[i:j+1]
            if sum(sub) == 0:
                dummy.append(sub)
    return dummy
# l = [1,4,-1,-4,6,-3,-3]
# a = sublist(l)
# print(a)
            

# Python code to remove duplicates elements in list
# Ex : [1,2,3,2,3] = [1,2,3]
# [], 1 -> add, 2 -> add, 3-> add, 2 -> will not add, 3 -> will not add
def rem_dup1(l):
    dummy = []
    for i in l:
        if i not in dummy:
            dummy.append(i)
    return dummy
# l = [1,2,3,2,3]
# a = rem_dup1(l)
# print(a)

def rem_dup2(l):
    dummy = []
    l1 = l.copy()
    for i in l1:
        if i not in dummy:
            dummy.append(i)
        else:
            l.remove(i)
# l = [1,2,3,2,3]
# a = rem_dup2(l)
# print(l)
    
    
# Given a list of items, remove duplicates and display in ascending order,return list type
# list -> set
# set -> list
def ord_dup(l):
    b = set(l)
    c = list(b)
    return c
# ans = ord_dup([4,3,5,6,1,4,3,7])
# print(ans)


# Tuple to String with seperator
# Ex :- (1,2,3), ":" => 1:2:3
# each element in tuple should be converted to string datatype
# those elements should be there inside list

def tup_to_str(tup,sep):
    l = [str(i) for i in tup]
    s = f" {sep} ".join(l)
    return s
def run():
    seperators = ["!","@","#","$","%","^","&","*","-","+","=",":",";","/","\\","|",",",".","?"]
    t = (1,2,3,4,5)
    for i in seperators:
        a = tup_to_str(t,i)
        print(a)
# run()

# Find min and max elements from tuple
# using methods :-
def min_max1(t):    # 2n - Time complexity
    return min(t),max(t)  
# a,b = min_max1((5,3,4,2,7,5))
# print(a,b)

# or

def min_max2(t):    # n*n = n^2 - Time complexity
    a = list(set(t)) 
    return a[0],a[-1]
# a,b = min_max2((5,3,4,2,7,5))
# print(a,b)

# or
# without using methods
def min_max3(t):    # n - Time complexity
    mini = t[0]
    maxi = t[0]
    for i in t:
        if i<mini:
            mini = i
        if i>maxi:
            maxi = i
    return mini,maxi
# a,b = min_max3((5,3,4,2,7,5))
# print(a,b)


# Return true if duplicates there or else return false
def is_dup_there(l):
    a = len(l)
    b = len(set(l))
    return a != b
# a = is_dup_there([1,2,3,5,1])
# print(a)


# Python code -> Tuple to dictionary with index
# Ex : input = ("a","b","c")
#      output = {"a" : 0,"b" : 1,"c" : 2}

def tup_to_dic1(t):
    dic = {}
    for i in t:
        dic[i] = t.index(i)
    return dic
# t = ("a","b","c","d")
# a = tup_to_dic(t)
# print(a)

def tup_to_dic2(t):
    return {i : t.index(i) for i in t}
# t = ("a","b","c","d")
# a = tup_to_dic2(t)
# print(a)


# Python code -> To count the occurances of elements in tuple
# input : (1,2,3,2,1)
# output : {1 : 2, 2 : 2, 3 : 1}
def count_occurances1(t):
    count_dic = {}
    for i in t:
        if i not in count_dic:
            count_dic[i] = 1
        else:
            count_dic[i] += 1
    return count_dic
# a = count_occurances1((1,2,3,2,1))
# print(a)

from collections import Counter
def count_occurance2(t):
    return dict(Counter(t))
# a = count_occurance2((1,2,3,4,1,4))
# print(a)


# Python code -> To filter the dictionary by keys with same specified prefix
# input : dic = {'apple':1,'banana':2,'appricot':3,'mango':4}, prefix = "ap"
# output : {'apple':1,'appricot':3}

def same_prefix1(dic,prefix):
    res_dic = {}
    pref_len = len(prefix)
    for key,value in dic.items():
        if key[:pref_len] == prefix:
            res_dic[key] = value
    return res_dic
# dic = {'apple':1,'banana':2,'appricot':3,'mango':4}
# prefix = "ap"
# a = same_prefix1(dic,prefix)
# print(a)

def same_prefix2(dic,prefix):
    res_dic = {}
    for key,value in dic.items():
        if key.startswith(prefix):
            res_dic[key] = value
    return res_dic
# dic = {'apple':1,'banana':2,'appricot':3,'mango':4}
# prefix = "ap"
# a = same_prefix2(dic,prefix)
# print(a)

def same_prefix3(dic,prefix):
    return {key : value for key,value in dic.items() if key.startswith(prefix)}
# dic = {'apple':1,'banana':2,'appricot':3,'mango':4,"appulu":5}
# prefix = "ap"
# a = same_prefix3(dic,prefix)
# print(a)

# https://www.codechef.com/problems/REMOVECARDS?tab=statement :-
# from collections import Counter
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split(" ")))
#     a = Counter(l)
#     # {1 : 2, 2 : 2,3 : 1}
#     # print(a.values())
#     b = max(a.values())
#     print(n-b)


# Prime number checker
# n=5 -> 1,2,3,4,5 -> ==1,5 | !=2,3,4 
# 2,n -> 2,3,4 -> n%i==0: return False,return True
def is_prime(n):
    if n==1:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
# ans = is_prime(4)
# print(ans)

n = 5
if n==1:
    print(True)
else:
    a = 0
    for i in range(2,n):
        if n%i == 0:
            a = 1
    if a==1:
        print(False)
    else:
        print(True)
        


