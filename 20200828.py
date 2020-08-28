# FIZZBUZZ with TDD
# 
# FizzBuzz is a well-known exercise that (according to Wikipedia) is a children's exercise, a 
# drinking game, and a developer interview question. It's lost some of its value as the latter 
# because pretty much everybody knows what it is and how to solve it, but it's still an interesting 
# problem with a few interesting solutions.
# Let's look at a few TDD approaches to the problem. I'm looking for a fizzbuzz function that takes 
# one positive integer parameter and decides whether to return Fizz, Buzz, or the integer.
# 
# ONE: the wrong approach
test.assertEquals(fizzbuzz(1), 1)
# fails as there's no code
def fizzbuzz(n):
    return 1
# makes it pass.
test.assertEquals(fizzbuzz(2), 2)
# fails as it currently returns 1
def fizzbuzz(n):
    if n == 1; return 1
    if n == 2; return 2
# passes both tests - but you can see where we're going here
test.assertEquals(fizzbuzz(3), "Fizz")
# Fails
def fizzbuzz(n):
    if n == 1; return 1
    if n == 2; return 2
    if n == 3; return "Fizz"
# passes all tests, but obviously this is not the way to go. Writing your function based on each 
# test case is a pitfall of TDD. The goal should be to make the code progressively more general 
# while the tests become more and more specific.
# 
# TWO: a better approach
# The first three tests will be the same so I'll just write three versions of the function each 
# based on the next test:
def fizzbuzz(n):
    return 1
# That's still a valid first version.
def fizzbuzz(n):
    return n
# Much better than requiring 2 if-statements
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    else:
        return n
# This passes the 4 case as well, but the 5 case fails:
test.assertEquals(fizzbuzz(5), "Buzz")
# So we write:
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n
# This passes the 5 case, and every case up to 15 where we get:
test.assertEquals(fizzbuzz(15), "FizzBuzz")
# So in order to pass this there are two options. We can define the exact n % 15 == 0 case, added 
# after the last elif conditional in the last version:
def fizzbuzz(n):
    ...
    elif n % 15 == 0:
        return "FizzBuzz"
    ...
# Or we can take the cumulative approach, like this:
def fizzbuzz(n):
    res = ""
    if n % 3 == 0:
        res += "Fizz"
    if n % 5 == 0:		# now elif doesn't work here anymore! Try it if you're unsure
        res += "Buzz"
    if not res:
        res = n			# I could say "return n" instead of assigning it, but I like having
    return res			# only one return in a function
# Either one of these now pass all of the tests. So far so good.
# 
# THREE: the cheater's approach
# It's not really cheating, of course. Python allows it, so it's valid. This solution hinges on two 
# characteristics: you can apply multiplication to strings, and booleans True and False have a 
# value of 1 and 0, respectively.
# Neither of these are unique to Python, by the way.
# Consider this:
print("Hello!" * 3)
# returns "Hello!Hello!Hello!". If I change the 3 to a 0, it wouldn't print anything. This means if 
# I use False instead of 0, that has the same result. This suggests that if I use a comparison that 
# evaluates to False, and therefore multiplies the string by 0, it returns nothing.
print("Hello!" * (5 < 3))
# The 5 < 3 comparator evaluates to False, which means the argument passed to print() is 
# "Hello!" * 0. Nothing is printed.
# We can use this in an interesting fizzbuzz solution.
def fizzbuzz(n):
    res = ""
    res += "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0)
    if not res:
        res = n
    return res
# It creates an empty variable res, then appends Fizz and/or Buzz depending on whether the 
# comparators n % 3 and/or n % 5 evaluate to True. If by the end of that line res is empty, it 
# assigns the parameter value instead.
# In order to get a list of FizzBuzz values you can now call this function for example like below:
for n in range(1, 100):
    print(fizzbuzz(n))
# There are even shorter solutions - although not much shorter - but this one strikes a nice 
# balance between short, smart, and readable for me.
