# I'd like to introduce a new concept, that isn't actually at all new but I
# thought of this cool name so just go with it alright?
# 
# THE HAUGHTY CORE
# The haughty core is kept separate from anything else in the system. The user
# interface (graphical or not), the database, and any other components only
# communicate with it through gateways: separate interface classes that handle
# incoming and outgoing communication with the core rules.
# 
# The core is haughty, because it does not care or even really know about any
# other components of the application. It comprises a set of rules that
# together make up all features of the app in question. These are highly
# logical and don't concern themselves with, among other things:
# 1. Displaying data
# 2. Receiving user input
# 3. Querying database
# 
# Let's take a simple calculator. Its core can only do a few things: add,
# subtract, multiply, divide. Each of these are a separate method in the
# 'calculate' class.
# In order to enter values and print results, you need a user interface. This
# is handled by a separate class. In order to pass the values entered by the
# user to the calculator, and to pass the result back to the user, I'm using a
# third class 'gateway'.
# 
# It seems excessive to write three entire classes for a simple calculator that
# only does four different operations. Of course this example is a little
# contrived - if you only want your app to do very basic addition, subtraction,
# etc there's absolutely no reason to separate the core from the UI like this.
# However, structuring it this way allows me to add or change features very 
# easily. I can write a GUI if I want to get away from the terminal, and that 
# GUI only needs to implement the gateway class in order to be effective. The 
# rest of the code doesn't change.
# If I want to add a memory feature that can store a result for later recall,
# I can write that as an additional feature to the existing core. Until I
# update the gateway and the UI, they are not going to care about this new
# feature - it does not affect them in any way.
# 
# Now that I have determined the three classes I want to write and I have some
# idea of the methods they need, I can use TDD to write them all and get great
# test coverage to boot.
# 
#
# 
######################
#### HAUGHTY CORE ####

class calculator():
    def add(self, *val):
        res = 0
        for v in val:
            res += v
        return res

    def subtract(self, *val):
        res = val[0] * 2
        for v in val:
            res -= v
        return res

    def multiply(self, *val):
        res = 1
        for v in val:
            res *= v
        return res

    def divide(self, *val):
        if len(val) == 1:
            return val[0]
        res = val[0] * val[0]
        for v in val:
            res /= v
        return res
