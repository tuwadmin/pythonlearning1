# # Tracking learning with Udemy Python course

# name = "Samia" #string
# age = 94 #integer
# height = 10.8 #float
# is_programmer = True #boolean

# print(name)
# print(age)
# print(height)
# print(is_programmer)

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_programmer))

# a = b = c = 10

# print(a)
# print(b)
# print(c)

# name, age, height, is_programmer = "Sam", 31, 5.2, False

# print(name)
# print(age)
# print(height)
# print(is_programmer)

# a, b = 5, 10

# print(a)
# print(b)

# birth_year = int(input('What is your birth year?'))
# current_year = 2026
# age = current_year - birth_year
# print('You are ', age, 'years old!')

# user_first_name = input('What is your first name?')
# user_last_name = input('What is your last name?')

# print('Hello, ', user_first_name, user_last_name, "! Welcome to Python Programming!")

# start_distance = float(input('Enter a distance in kilometers!'))
# kilometers_to_miles = start_distance*0.621371
# print(kilometers_to_miles)

# syntax

# Tuples
# tuplename = (element1, element2, element3 ...)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# tuple operations

# access tuple elements using index

print(my_tuple[1])

tuple_2 = (6, 7)
new_tuple = my_tuple + tuple_2
print(new_tuple)

# tuples are immutable, cannot change content

# Lists
# Lists are mutable, can be changed

# listname = [element1, element2, element3]

my_list = [1, 2, 3, 4, 5, "red", "green", "blue"]
print(my_list)

print(my_list[1])
print(my_list[2])

my_list.append("house")

print(my_list)

my_list.remove(3)
print(my_list)

print(my_list[1:4])
print(my_list)

print(my_list[5])
my_list[5] = "white"
print(my_list)


# Dictionaries
# dictionaries are mutable

# dict = {key1:value1, key2:value2, key3:value3}

my_dictionary = {'name': 'Ralph', 'age': 30, 'city': 'New York'}
print(my_dictionary)
print(my_dictionary['name'])
print(my_dictionary['city'])

my_dictionary['job'] = 'Engineer'
print(my_dictionary)

del my_dictionary['age']

print(my_dictionary)

my_dictionary['city'] = 'Albany'
print(my_dictionary)


# Sets
# sets do not allow duplicates

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(4)
print(my_set)

set1 = {1, 2, 3}
set2 = {4, 5, 6}

union = set1 | set2
print(union)

intersection = set1 & set2

print(intersection)

difference_set1 = set1 - set2
difference_set2 = set2 - set1

print(difference_set1)
print(difference_set2)