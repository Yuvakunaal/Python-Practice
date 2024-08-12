# Sets : Collection of ordered values without duplicates => {} 

s = {6,5,3,4,1,2,6,2,11}
print(s)

# add
s.add(9)
print(s)

# update : joins existing set
a = [8,11,12,5]
s.update(a)
print(s)

# remove : if you try to remove any element which doesnt exist.. error
s.remove(11)
print(s)

s.add(11)

# discard : if you try to remove any element which doesnt exist.. no error
s.discard(14)
print(s)

# Looping over sets
for i in s:
    print(i)
    
# joining two sets :- (union : joins and stores in new variable)
s1 = {1,2,3}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s1)
print(s2)
print(s3)

# copy :-
s = {1,2,3,4}
sdup = s.copy()
print(sdup)

print()
# set operations 
# union, intersection,difference
# union : gives all combined sets
# intersection : gives all common combined sets
# difference : gives non-common from first given set

s1 = {1,2,3,4}
s2 = {3,4,5,6}

union = s1 | s2
intersection = s1 & s2
diff_s1 = s1 - s2
diff_s2 = s2 - s1

print(f"{union}\n{intersection}\n{diff_s1}\n{diff_s2}")
