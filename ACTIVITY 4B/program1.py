A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

union_A_B = A | B
intersection = A & B
print("a. How many elements are there in set A and B?")
print(len(union_A_B), union_A_B)
print(len(intersection), intersection)
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

print("h, i, j, k:", hijk)
print("c, d, f:", cdf)
print("b, c, h:", bch)
print("d, f:", df)
print("c:", c_only)
print("l, m, o:", lmo)