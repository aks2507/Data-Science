# Q2
lst1 = [1, 2, 3, 4, 5]
lst2 = lst1.copy()

for i in range(len(lst2)):
    lst2[i] = 2 * lst2[i]
print(lst1)
print(lst2)
