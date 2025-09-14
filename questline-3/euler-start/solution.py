# sum of all multiples of 3 or 5 below 1000

print("problem 1")
s= 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(s)


#fibonacci even sequence sum (starting at 1,2, ..)

print("problem 2")
a,b=1,2
t=0
while a<+4000000:
    if a%2==0:
        t+=a
    a,b=b,a+b

print(t)
