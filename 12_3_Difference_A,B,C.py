# Дано три множества
# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) виполнить difference єтих множеств

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
print('вариант 1:', set1 - set2 - set3, set2 - set1 - set3, set3 - set2 - set1)
print('вариант 2:', set1.difference(set2, set3), set2.difference(set1, set3),
      set3.difference(set2, set1))