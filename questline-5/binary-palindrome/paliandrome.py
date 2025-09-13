# palindrome.py
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for num in (num1, num2):
    binary = bin(num)[2:]  #  remove '0b'
    result = "Palindrome" if binary == binary[::-1] else "Not Palindrome"
    print(f"{num} in binary: {binary} -- {result}")
