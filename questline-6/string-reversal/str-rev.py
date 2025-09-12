# str_rev.py

txt = "hello"
print("Original String:", txt)

# Iterative method
rev_str = ""
for ch in txt:
    rev_str= ch +rev_str # append each character
print("iterative case",rev_str)

# Recursive method
def rev_rec(txt):
    if len(txt) <= 1:  # base case
        return txt
    return rev_rec(txt[1:]) + txt[0]  # reverse rest + first char


print("Recursive Reverse:", rev_rec(txt))
