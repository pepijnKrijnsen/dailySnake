# THE MAGIC OF POLYMORPHISM
# 
# Okay, so that's overstating things. Polymorphism is not magic. It's just a very cool concept that 
# makes much of Python work very seamlessly. Let's explore it in a little detail.
# 
# The len() function can return the length of any iterable object. It doesn't care about the type 
# of object.
string = "string"
print(len(string))
# return 6
tuple = (1, 1, 2, 3, 5, 8)
print(len(tuple))
# returns 6
# The reason that this works is because len() doesn't care about the class that an object is part 
# of, or any of the methods or attributes of that object other than the one it needs to return the 
# length of the object in question.
# 
# An oft-repeated adage is that everything in Python is an object. When I assigned the string above
# it generated a string object with - among other things - the contents and length of the string.
# Let's see if we can simulate some of this behaviour in order to understand polymorphism better.
# 
# First I'm going to create a custom len() function called length().
def length(obj):
	return obj.number_of_elements
# 
# Now let's create a "CustomString" class with "contents" and "number_of_elements" attributes:
class CustomString:
	def __init__(self, contents, number_of_elements):
		self.contents = contents
		self.number_of_elements = number_of_elements
# 
# Now let's create an instance of this class
greeting = CustomString("Hello", 5)
# creates an instance of this class with contents equal to "string" and number_of_elements equal to 
# 5 and binds that to the variable "greeting".
# (Before you ask how the object would know the length of the string being created: I'm not sure of 
# the exact C code going on under the hood, but this is something that can be recorded as the 
# string is constructed.)
# Let's create another class for creating tuples:
class CustomTuple:
	def __init__(self, contents, number_of_elements):
		self.contents = contents
		self.number_of_elements = number_of_elements
# 
# and create an instance of this, too:
numbers = CustomTuple("1 1 2 3 5 8", 6)
# With both of these created, let's see what happens when I pass them both to my custom length() 
# function:
print(length(greeting))
print(length(numbers))
# This confirms that my custom Length() function does not care about the object it is being passed. 
# It just tries to retrieve the number_of_elements attribute without first checking the type of its 
# argument.
# 
# The same technique can be used to separate different parts of a system. An interface-like object 
# (Python doesn't have a distinct interface keyword like for example Java, but it can be simulated) 
# can help to keep parts of a system that have different roles separate and decoupled from each 
# other.
# I'll explore this in much more detail next week using my stupid calculator from earlier files as
# an example. Right now it's a poor implementation of model-view-controller - if that - and we'll
# see if I can turn that into a proper decoupled system with elements communicating through an
# interface.
