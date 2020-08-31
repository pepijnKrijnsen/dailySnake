# INTERFACED
# 
# As mentioned on the 29th, polymorphism can be used to create interfaces for other classes.
# As mentioned on the 27th, the current gateway class of my calculator app is a big mess of 
# procedural code that's just asking to be refactored.
# While this may result in a nice model-view-controller split, it's not the same as a core of 
# business rules separated by interfaces.
# 
# Interfaces are great to interact with private classes. The class can be completely hidden, hiding 
# its implementation. The user (or other services) interact with it only through an interface.
# Python doesn't have invisible classes in the same way that for example Java uses private classes, 
# but simulating the same behaviour can still be worthwhile. Python can be used to set up pretty 
# massive systems, if required - and such systems need a proper architecture.
# 
# When I'm writing things like the bug tracker app I'm working on, or a gardening app for Anna to 
# keep track of things, I don't really need a massive focus on architecture. It can help - but it's 
# easy to overthink, and in no way necessary for something that will never grow into a large 
# system.
# No matter how big those apps get, they will never be entire systems with extensive I/O, hundreds 
# (or even dozens) of users, etc. They're just little projects. I'm not saying architecture is not 
# important even in that case - I'm just saying that planning for the eventuality that I'll need to 
# build an opera house when all I'm trying to do is build a shed may be overkill.
# So, let's refactor the gateway() class from my calculator - starting by giving the class a 
# different name.
# 
# The main problem is that the gateway class is acting as the event loop and main() method - the 
# app is literally started by calling
c = gateway()
# which doesn't make much sense. Really the program should call main() and things should start 
# rolling from there.
class main():
    def __init__(self):
        title = "\n\nTHE STUPID CALCULATOR\n\n"
        UI.output(title)
        calculate.start(calculate)
# 
# And the calculate class now looks like this:
class calculate():
    
    def start(self):
        act = "Do you want to:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide?\n"
        op = UI.input(act)
        valid_choices = ("1", "2", "3", "4", "add", "subtract", "multiply", "divide")
        while op not in valid_choices:
            error_wrong_choice = "That choice was not recognised - please try again\n"
            UI.output(error_wrong_choice)
            op = UI.input(act)
        
        values = self.getValues()
        result = self.getResults(op, values)
        UI.output(result)
        print("\n")
        if self.again():
            self.start(self)
        
        
    def getValues():
        vals = None
        while not vals:
            which_values = "Which values, in which order? (Use spaces to separate)\n"
            vals = UI.input(which_values)
            try:
                vals = vals.split()
                for i,v in enumerate(vals):
                    vals[i] = float(v)
            except:
                vals = None
                error_wrong_value = "Those are not numbers - please try again\n"
                UI.output(error_wrong_value)
        return vals
        
    def getResults(op, vals):
        if op == "1" or op == "add":
            res = operate.add(*vals)
        elif op == "2" or op == "subtract":
            res = operate.subtract(*vals)
        elif op == "3" or op == "multiply":
            res = operate.multiply(*vals)
        elif op == "4" or op == "divide":
            res = operate.divide(*vals)
        else:
            UI.output("In the words of Lee Mack: how did that happen!?")
        return res

    def again():
        more_work = "Do you have more numbers to do? (Empty for no) "
        return UI.input(more_work)
# 
# Still big, but makes much more sense now - and the program is started by simply calling main(), 
# which prints the title and then hands control to the calculate method.
# 
# Starting tomorrow I'll be looking at recursion - again, cos hey, it's interesting! - and we'll
# see where we go from there.
