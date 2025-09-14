#caeser_cipher.py

# Encode RECRUIT with +3
encoded = ""

for i in ("RECRUIT"):
    encoded += chr((ord(i) + 3))

print("Encoded 'RECRUIT' (+3):", encoded)

# Decode ZHOFRPH with -3
decoded = ""

for j in ("ZHOFRPH"):
    decoded += chr((ord(j) - 3))
print("Decoded 'ZHOFRPH' (-3):", decoded)
