
def unique(total):
    new_total = []
    for i in total:
        if i not in new_total:
            new_total.append(i)
    print("The unique numbers of the list is: ", new_total)
    count = len(new_total)
    return count



x = int(input("Enter the number of elements: "))
total = []
for i in range(x):
    y = int(input("Enter the numbers: "))
    total.append(y)
print("The list is: ",total)
a = unique(total)
print("Number of unique numbers in the list is: ",a)
