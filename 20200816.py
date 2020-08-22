# Passing data to Python functions
# 
# 1. A function can receive a float, integer, or literal string as data
def passRawData(a):
  print(a)

passRawData(42)
# returns 42

passRawData("Hello, world!")
# returns "Hello, world!"

# 2. A function can receive a variable as data
def passVariable(a):
  print(a)

num = int(42)
str = "Hello, world!"

passVariable(num)
# returns 42

passVariable(str)
# returns "Hello, world!"

# 3. A function can receive a variable that contains a list or tuple; and, if
# the number of elements in the list or tuple matches the number of arguments
# expected by the function, the elements of the list or tuple can be unpacked
# to be used as individual parameters.
def passTuple1(some_numbers):
  for v in a:
    print(v)

a = (1, 2, 3)

passTuple1(a)
# returns 1, 2, 3 each on their own line

def passTuple2(num1, num2):
  print(num1 * num2)

a = (2, 4)

passTuple2(*a)
# returns 8
# the asterisk operator unpacks the tuple into its constituent elements and
# passes those to the function as arguments.

# 4. A function can use the return value of another function as a parameter,
# and the function being used as a parameter can receive its own parameters.
def passFunction(a):
  print(a)

def funcToPass1():
  return("Hello, GitHub!")

passFunction(funcToPass())
# returns "Hello, GitHub!" - please note that if you call this as
passFunction1(funcToPass)
# the first function will print the memory address of the function
# object named 'funcToPass', instead of calling the function

def funcToPass2(a):
  return a

passFunction(funToPass2("Hello, sillies!"))
# returns "Hello, sillies!"

# Parameters being passed to the function being used as a parameter of another
# function need to be visible only to the function that actually needs them.
# In other words, in the function call
funcOne(funcTwo(var))
# the variable 'var' needs to be visible to funcTwo, but not necesarily funcOne.

a = 42

passFunction(funcToPass2(a))
# returns 42, and would still return 42 if the variable a was in a different scope
# than passFunction, and EVEN if there was a different variable called a in the same
# scope as passFunction.
