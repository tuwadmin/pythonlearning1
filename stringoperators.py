# string concatenation

first_name = "John"
last_name = "Doe"

full_name = first_name+' '+last_name
print(full_name)


# String Repetition
word = "Hello"
repeat_count = 3

repeated_work = word*repeat_count

print(repeated_work)

# String Comparison

fruit1 = 'apple'
fruit2 = 'tangerine'

print(fruit1 == fruit2)
print(fruit1!=fruit2)
print(fruit1 > fruit2)
print(fruit1 <fruit2)
print(fruit1>=fruit2)
print(fruit1 <= fruit2)

# String Membership Operators

sentence = 'The quick brown fox jumps over the dog'
print('quick' in sentence)
print('dog' in sentence)
print('Quick' in sentence)

# String Slicing or Indexing

text = 'Hello, World!'

# Extract the word Hello from the string text

extracted_string = text[0:5]
print(extracted_string)