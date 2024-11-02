my_dict = {'Hanna':1999, 'Joseph':2004, 'Daphna':2010, 'Bred':1993}
print(my_dict)
print(my_dict['Hanna'])
print(my_dict.get('Zazi', 'Такого значения нет'))
my_dict['Ted'] = 2024
my_dict['Lucy'] = 2008
values_ = my_dict.get('Daphna')
my_dict.pop('Daphna')
print(values_)
print(my_dict)

my_set = {'String', 1 ,2, 3, 4,'String', 4, 1, 2,'String', 3, 3, 3, 1, 2, 3,'String'}
print(my_set)
my_set.add(8)
my_set.add(False)
my_set.remove(1)
print(my_set)
