colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))

sundry = ['John', 3.14, 7, False]
print(sundry)
print(type(sundry))

my_list = []

# ***************************************************************************************************

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')

# ****************************************************************************************************

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')

print(f'Next to last item in the list: {colors[-2]}')

# ****************************************************************************************************

colors.reverse()
print(colors)

colors.sort()
print(colors)

# ***************************************************************************************************

print(colors)

color = colors.pop(0)
print('popped', color)

print(colors)

# ***************************************************************************************************

print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

# ****************************************************************************************************

new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(colors)

# ***************************************************************************************************

print(colors)
colors.clear()
print(colors)