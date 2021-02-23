import processor1

my_list = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
my_bad_list = 5

numbers = processor1.process_numbers(my_list)
print(numbers)

names = processor1.process_names(my_list)
print(names)

numbers = processor1.process_numbers(my_bad_list)
print(numbers)

names = processor1.process_names(my_bad_list)
print(names)