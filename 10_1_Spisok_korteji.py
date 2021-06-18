#Дано список словорей, создать список кортежей.

list_dict = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
result = [tuple(val.values()) for val in list_dict]
print(result)
