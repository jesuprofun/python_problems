

def largest(numbers):
    great = 0
    for i in numbers:
        if i > great:
            great = i
    return great



x = int(input("Enter the number of elements: "))
total = []
for i in range(x):
    y = int(input("Enter the numbers: "))
    total.append(y)
print(total)
big = largest(total)
print("The largest number in the list is:",big)
