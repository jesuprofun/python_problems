
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40, 50, 60]
l3 = [100, 200, 300, 400, 500, 600]

l4 = list(map(lambda x, y, z : x + y - z, l1, l2, l3))

print(l4)
