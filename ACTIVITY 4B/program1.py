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

hijk = list(C - A)
hijk.sort()

cdf = list(A & C)
cdf.sort()

bch = list((A & B) | (B & C))
bch.sort()

df = list((A & C) - B)
df.sort()

c_only = list(A & B & C)
c_only.sort()

lmo = list(B - (A | C))
lmo.sort()

print("c. Show the following using set operations:")
print(f"i.   {hijk}")  
print(f"ii.  {cdf}")    
print(f"iii. {bch}")    
print(f"iv.  {df}")    
print(f"v.   {c_only}") 
print(f"vi.  {lmo}")  