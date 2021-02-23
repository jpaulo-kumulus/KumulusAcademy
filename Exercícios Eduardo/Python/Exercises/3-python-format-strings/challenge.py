first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
len(first_value.strip())
print(first_value.strip().title().rjust(22))

# Second challenge
print(second_value.replace('-', ' ').strip().capitalize())

# Third challenge
leng3 = len(third_value.replace(' ', '')) + len(second_value.replace('-', ' ').strip()) - 1
print(third_value.replace(' ', '').replace('-', ' ').capitalize().rjust(leng3))


# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value + '#' + fifth_value + '#' + sixth_value + '!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'.{fourth_value:^20}'  '\n'  f'.{fifth_value:^20}' '\n' f'.{sixth_value:^20}')
