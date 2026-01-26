# for loop

# 5 books
# b1, b2, b3, b4, b5

for i in range(5):
    print(i)

# i is iterated from 0-4
# 5 times

# while loop - condition is true

count = 0
while count < 5:
    print(count)
    count +=1

for number in range (21):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

nums = [14, 15, 22, 29, 35, 42, 50]

for num in nums:
    if num % 7 == 0:
        print('True')
    else: 
        print('False')
    break
