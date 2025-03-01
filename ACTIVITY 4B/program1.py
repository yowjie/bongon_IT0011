A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

union = A | B
B_not_A_C = B - (A | C)

print("a. How many elements are there in set A and B?")
print(len(union), list(union))
print()

print("b. How many elements are there in B that is not part of A and C?")
print(len(B_not_A_C), list(B_not_A_C))
print()

hijk = sorted(C - A)  
cdf = sorted(A & C)  
bch = sorted((A & B) | (B & C))  
df = sorted((A & C) - B)  
c_only = sorted(A & B & C)  
lmo = sorted(B - (A | C))  

print("c. Show the following using set operations:")
print("i.  ", hijk)  
print("ii. ", cdf)    
print("iii.", bch)    
print("iv. ", df)    
print("v.  ", c_only) 
print("vi. ", lmo)    