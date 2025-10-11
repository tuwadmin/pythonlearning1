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

# creating lists

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]
total = ratings_1 + ratings_2 + ratings_3
average = total/3

# negative indexes

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]

total_rating = rating_1+rating_2+rating_3
average_rating = total_rating/3

# calculate average of isolated indexes

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
2
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
3
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
4
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
5
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
6
​
7
fb_rating_data = [row_1[0], row_1[3], row_1[4]]
8
insta_rating_data = [row_2[0], row_2[3], row_2[4]]
9
pandora_rating_data = [row_5[0], row_5[3], row_5[4]]
10
​
11
avg_rating = (fb_rating_data[2]+insta_rating_data[2]+pandora_rating_data[2])/3

# dataset index isolation and averages

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1,row_2,row_3,row_4,row_5]
avg_rating = ((app_data_set[0][-1])+(app_data_set[1][-1])+(app_data_set[2][-1])+(app_data_set[3][-1])+(app_data_set[4][-1]))/5

# Open, read and close files

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
print(read_file[:300])
opened_file.close()

# use splits to separate lists by breaks/characters

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
new_line_split = read_file.split("\n")
opened_file.close()

header = (new_line_split[0].split(","))
data_row_1 = (new_line_split[1].split(","))
data_row_2 = (new_line_split[2].split(","))
first_three_lists =[header,data_row_1,data_row_2]
print(first_three_lists)

# looping through a list


header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]
first_three = [header, data_row_1, data_row_2]

index=0
for value in first_three:
    first_three[index] = value.split(",")
    print(first_three[index])
    index += 1

print(first_three)

# reading CSV files

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

print(len(apps_data))
print(apps_data[0])
print(apps_data[1],apps_data[2])

# loop through list and average ratings

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0

for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating
    
print(rating_sum)

avg_rating = rating_sum/7197

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

all_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    all_ratings.append(rating)
    

avg_rating= sum(all_ratings)/len(all_ratings)

print(avg_rating)
    