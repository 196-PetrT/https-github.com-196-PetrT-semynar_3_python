# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
 {" VIII": " S007 "}]

list_2 = set()
# традиционный итератор с функцией add() для множества
for i in list_1:
    for v in i.values():
        list_2.add(v)
print(list_2)
# или множественное включение set comrehension
print(set(v for i in list_1 for v in i.values()))

