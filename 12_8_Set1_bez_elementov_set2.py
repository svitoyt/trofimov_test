# Учитывая два набора Python, обновите первый набор элементами,
# которые существуют только в первом наборе, но не во втором наборе.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1 = set1 - set1.intersection(set2)
print(set1)