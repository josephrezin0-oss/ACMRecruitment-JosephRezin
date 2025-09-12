
print("og list [5,2,9,1,5,6]")
data = [5, 2, 9, 1, 5, 6]
n = len(data)                                      #no of items in list=n
for i in range(n):                                 #for range of 6
    for j in range(0, n - i - 1):                  
        if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]#swapping if elements found next is greater than current value


print("Sorted List:", data)

