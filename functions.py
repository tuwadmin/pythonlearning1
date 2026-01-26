# definition

def say_hello():
    print('Hello World!')

# say_hello()

print('Hello Alice')
print('Hello Bob')
print('Hello Charlie')

def greet(name):
    print('Hello', name)

greet('Alice')
greet('Bob')
greet('Charlie')

def add(a,b):
    print('sum:', a+b)

add(3,5)

def greet(name = "Guest:"):
    print('Hello,', name)

greet('Alice')

def square(num):
    return num * num

result = square(4)
print("Square of 4 is:", result)
