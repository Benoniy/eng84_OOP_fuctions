# Functions
### What are functions?  
  ***Functions are blocks of code that are set up to help a developer keep their code "DRY".***  
  ***This means "Don't Repeat Yourself", by using functions we can minimise the clutter in***  
  ***code and increase the flexibility of our programs.***
* Standard declaration
```python
# Definition of the function
def hello():
    print("Hello World")
    
hello() # Function call
```  
* Functions can take arguments  
```python
# Functions can take any number of arguments
def add_num(num1, num2):
    print(num1 + num2)

add_num(10, 5) # Function call
```
* `return` - a key aspect of functions that parses a value back  
```python
def sub_num(num1, num2):
    return num1 - num2  # This terminates the function

result = sub_num(10, 5)  # Function return is stored in this variable
print(result)
```  

### What are some use cases for functions?  
* To prevent the repetition of code  
* To allow for greater flexibility of code  
* To modularise code making it easier to edit  