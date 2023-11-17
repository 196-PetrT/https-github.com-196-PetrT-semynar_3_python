# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]

res = []
for i in list_1:
    if i not in res:
        res.append(i)
print(res)
print(len(res))

# print(len(set(list_1)))

