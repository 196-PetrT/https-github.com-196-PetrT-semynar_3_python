# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
k = 3
shift = 0
buf = int
while shift < k:
    buf = list_1.pop(len(list_1)-1)
    list_1.insert(0, buf)
    shift += 1

print(list_1)

# lst = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     lst.insert(0, lst.pop())
# print(lst)

