# and

# c1 and c2

age = 20
citizenship = True
if age >= 18 and citizenship:
    print('Eligible to vote')

# or

age = 27
has_permission = True
if age >= 18 or has_permission:
    print('You can go to the concert')

# Not

is_snowy = False
if not is_snowy:
    print('It is warm outside.')

user_input1 = input(int())
user_input2 = input(int())
user_input3 = input(int())

if user_input1 >= user_input2:
    print('Wow, ', user_input1, ' is a big number!')
elif user_input2 > user_input3:
    print('Wow, ', user_input2, ' is a big number!')
else: 
    print('Wow, ', user_input3, ' is a big number!')

