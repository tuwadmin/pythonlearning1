# addition
result = 20

result = result + 10

print(result)

# compound addition

result += 10

print(result)

# assign variables and compound add or multiply
variable_1 = 5
variable_2 = 10

variable_1 += 5
variable_2 *= 10

print(variable_1, variable_2)

# float = convert to decimal
# int = round down regardless if over .5
# round = round up depending on if over or under .5

print(float(2))
print(int(4.7))
print(int(4.1))

print(round(4.1))
print(round(4.8))

variable_a = 13.9
variable_b = 2.8
variable_a = round(variable_a)

variable_b = int(variable_b)

print(variable_a, variable_b)

# assigning strings
app_name = 'Pandora - Music & Radio'
average_rating = '4.0'
total_ratings = '1724546'
price = 'free'
print(app_name)

# disregarding special characters with backslash \

slogan = 'Mega\'s AI slogan is \"Explore. Create. Do More."'
print(slogan)

# using 3 single quotes to disregard special character rules '''

facebook = '''Facebook's rating is'''
fb_rating = float(3.5)
fb_rating_str = str(fb_rating)

fb = facebook + ' ' + fb_rating_str
print(fb)