# Python Key Concepts

# 1. Basic Syntax
print("Hello, Python!")  # Output text
name = input("What is your name? ")  # Input text
print(f"Nice to meet you, {name}!")  # String formatting

# 2. Control Flow
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

for i in range(3):
    print(f"Loop {i}")

while x > 0:
    print(x)
    x -= 1

# 3. Data Structures
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {"a": 1, "b": 2}
my_set = {1, 2, 3, 2}  # Duplicates are removed

print(my_list, my_tuple, my_dict, my_set)

# Iteration and Mutation - List
print("Original list:", my_list)
for i in range(len(my_list)):
    my_list[i] *= 2  # Mutate each element
print("Mutated list:", my_list)

# Iteration and Mutation - Dictionary
print("Original dictionary:", my_dict)
for key in my_dict:
    my_dict[key] += 10  # Mutate each value
print("Mutated dictionary:", my_dict)

# 4. Functions
def add(a, b):
    return a + b

result = add(2, 3)
print(f"2 + 3 = {result}")

# 5. Modules and Libraries
import math

print(f"Square root of 16 is {math.sqrt(16)}")

# 6. File Handling
with open("example.txt", "w") as f:
    f.write("Hello, file!")

with open("example.txt", "r") as f:
    print(f.read())

# 7. Error and Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This runs no matter what")

# 8. Object-Oriented Programming
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a noise"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Rex")
print(dog.speak())

# 9. Working with Data
string = "Hello, world!"
print(string[:5])  # Slicing
print(string.upper())  # Uppercase

squares = [x**2 for x in range(5)]  # List comprehension
print(squares)

