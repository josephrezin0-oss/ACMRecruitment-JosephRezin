def rot_bin(bnry_str, k):
    for i in bnry_str:
        k = k % len(bnry_str)
        r= bnry_str[-k:] + bnry_str[:-k]
        valu = int(r, 2)
        return valu


bnry=str(input("enter binary "))
s = int(input("enter k to be rotated:"))
result = rot_bin(bnry, s)
print("Rotated binary:", bnry[-s:] + bnry[:-s])
print("Decimal value:", result)
