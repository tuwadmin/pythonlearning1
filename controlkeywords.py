#  Break - stop the loop immediately

movies = ["Jurassic Park", "LOTR", "Avatar", "Interstellar"]

for movie in movies: 
    print('Now watching: ', movie)
    if movie == "LOTR":
        print('Found my favorite movie, stopping the marathon!')
        break

# Continue
# Skip remaining code in the current iteration

dishes = ['Chicken Biryani', 'Samosas', 'Spagetti', 'Spicy Wings', 'Spicy Quesadillas']
for dish in dishes:
        if 'Spicy' in dish:
            print("Skipping:", dish)
            continue
        print('Eating: ', dish)

# Pass
# placeholder for possible future logic

tasks = ['Vacuuming', 'Studying', 'Coding', 'Skip']
for task in tasks:
     if task == 'Skip':
        pass
     else:
        print('Doing task', task)


