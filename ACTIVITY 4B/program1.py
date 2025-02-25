A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

union = A.union(B)
print("a. How many elements are there in set A and B?")
print(len(union), union)
print()

B_not_A_C = B - (A | C)
print("b. How many elements are there in B that is not part of A and C?")
print(len(B_not_A_C), B_not_A_C)
print()

print("c. Show the following using set operations:")
hijk = C - A - B
cdf = A & C
bch = (A & B) | (B & C)
df = (A & C) - B
c_only = A & B & C
lmo = B - (A | C)

print("i.", hijk)
print("ii.", cdf)
print("iii.", bch)
print("iv.", df)
print("v.", c_only)
print("vi.", lmo)