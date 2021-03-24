# What is a function
# def is used to declare a function
def hello():
    print("Hello World")


# Function call
hello()


# functions can take arguments
def hello_user(name):
    print(f"Hello {name}")


# Function call with an argument
hello_user("Ben")


# Functions can take any number of argument
def add_num(num1, num2):
    print(num1 + num2)


# Function call
add_num(10, 5)


# A key aspect of functions is the return keyword
def sub_num(num1, num2):
    return num1 - num2


# Function call
print(sub_num(10, 5))


# Exercise - create a basic calculator using functions and display appropriate messages for operations
# addition function
def add(x, y):
    return x + y


# subtraction function
def sub(x, y):
    return x - y


# multiplication function
def mult(x, y):
    return x * y


# division function
def divide(x, y):
    return x / y


a = 10
b = 5
print("If a = 10 and b = 5")
print(f"a + b = {add(a,b)}")
print(f"a - b = {sub(a, b)}")
print(f"a * b = {mult(a, b)}")
print(f"a / b = {divide(a, b)}")


# Exercise - Create a function that takes a user name (input) and displays a greeting message
def hello_user_input(name):
    print(f"Hello {name}")


# Function call with an argument
hello_user_input(input("What is your name?: "))
