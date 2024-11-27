# Python Key Concepts

# 0. Integers and Strings
def integers_and_strings():
    # Integers
    a = 10
    b = 5
    print(f"Integer a: {a}, Integer b: {b}")
    print(f"a + b = {a + b}")  # Addition of integers

    # Strings
    str1 = "Hello"
    str2 = "World"
    print(f"String 1: {str1}, String 2: {str2}")
    print(f"Concatenation: {str1 + ' ' + str2}")  # Adding strings (concatenation)
    print(f"String length of '{str1}': {len(str1)}")


# 1. Basic Syntax
def basic_syntax():
    print("Hello, Python!")  # Output text
    name = input("What is your name? ")  # Input text
    print(f"Nice to meet you, {name}!")  # String formatting


# 2. Control Flow
def control_flow():
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
def data_structures():
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
def functions_example():
    def add(a, b):
        return a + b

    result = add(2, 3)
    print(f"2 + 3 = {result}")


# 5. Modules and Libraries
def modules_and_libraries():
    import math
    print(f"Square root of 16 is {math.sqrt(16)}")


# 6. File Handling
def file_handling():
    with open("example.txt", "w") as f:
        f.write("Hello, file!")

    with open("example.txt", "r") as f:
        print(f.read())


# 7. Error and Exception Handling
def error_handling():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    finally:
        print("This runs no matter what")


# 8. Object-Oriented Programming
def object_oriented_programming():
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
def working_with_data():
    string = "Hello, world!"
    print(string[:5])  # Slicing
    print(string.upper())  # Uppercase

    squares = [x**2 for x in range(5)]  # List comprehension
    print(squares)


# Main function to call all examples
def main():
    print("\n0. Integers and Strings")
    integers_and_strings()

    print("\n1. Basic Syntax")
    basic_syntax()

    print("\n2. Control Flow")
    control_flow()

    print("\n3. Data Structures")
    data_structures()

    print("\n4. Functions")
    functions_example()

    print("\n5. Modules and Libraries")
    modules_and_libraries()

    print("\n6. File Handling")
    file_handling()

    print("\n7. Error and Exception Handling")
    error_handling()

    print("\n8. Object-Oriented Programming")
    object_oriented_programming()

    print("\n9. Working with Data")
    working_with_data()


