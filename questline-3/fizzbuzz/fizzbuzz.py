#pritnts 1 to 50 with multiples of 3 as"fizz" of 5 as"buzz" and of 3 and 5 as "fizzbuzz"

for i in range (1,51):
    if i%3 ==0 and i%5==0:
        print("fizzbuzz")
    elif i%3 ==0:
        print("fizz")
    elif i%5 ==0:
        print("buzz")
    else:
        print(i)
