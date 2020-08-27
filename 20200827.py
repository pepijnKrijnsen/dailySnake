# CALCULATOR FROM HAUGHTY CORE, pt. 2
# 
# Yesterday's calculator class only contains the very basic logic + - * / that allows it to perform 
# the operations every calculator should be capable of. However, there is no way to interact with 
# it.
# Let's create a user interface class to help.
class UI():
    def out(text):
        print(text)

    def in(text):
        v = input(text)
        return v
# 
# ...and that's all, folks! The UI literally only takes care of two things: it can print messages 
# to the user without returning any value, or it can ask the user for input.
# Note that the UI class does not do any input validation, either. Whatever input the user provides
# is passed straight on to the gateway class. The gateway (as we'll see below) checks the input and
# triggers the appropriate response. This is also why the core does not need to check its inputs:
# if the gateway passes on information, it is guaranteed to be correctly formatted (assuming that I
# wrote it correctly of course), and the core doesn't receive input from anywhere else.
# These methods demonstrate the extend to which the UI is allowed to influence the core. The UI is 
# not aware of anything outside of its own two tasks. None of the calculator's logic is stored in 
# this class. The UI does not ask for input, and call another function based on that; it certainly 
# doesn't ask for input and then performs an operation on it.
# This is where the gateway comes in. The gateway handles communication between the core and the 
# UI. This is a result of a few dozen cycles of TDD but without any refactoring, so it is a big 
# beast right now.
class gateway():

    def __init__(self):
        title = "\n\nTHE STUPID CALCULATOR\n\n"
        UI.output(title)
        self.calculate()
        
    def calculate(self):
        act = "Do you want to:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide?\n"
        valid_choices = ("1", "2", "3", "4", "add", "subtract", "multiply", "divide")
        error_wrong_value = "Those are not numbers - please try again\n"
        error_wrong_choice = "That choice was not recognised - please try again\n"
        vals = None

        o = UI.input(act)
        while o not in valid_choices:
            UI.output(error_wrong_choice)
            o = UI.input(act)
        while not vals:
            vals = UI.input("Which values, in which order? (Use spaces to separate)\n")
            try:
                vals = vals.split()
                for i,v in enumerate(vals):
                    vals[i] = float(v)
            except:
                vals = None
                UI.output(error_wrong_value)
        if o == "1" or o == "add":
            res = calculator.add(*vals)
        elif o == "2" or o == "subtract":
            res = calculator.subtract(*vals)
        elif o == "3" or o == "multiply":
            res = calculator.multiply(*vals)
        elif o == "4" or o == "divide":
            res = calculator.divide(*vals)
        else:
            UI.output("In the words of Lee Mack: how did that happen!?")
        UI.output(res)
        print("\n")
        self.again()

    def again(self):
        more_work = "Do you have more numbers to do? (Empty for no)"
        again = UI.input(more_work)
        if again:
            self.calculate()
# 
# If the UI were to change from CLI to GUI the UI class would change, because it would now have 
# multiple different options for output (multiple text fields) and input (multiple buttons) that 
# would need to be differentiated between. The gateway would need to add calls to the new UI 
# methods in order to get data in the right places, but the core would not change in any way: it 
# would not know or care about the change in UI.
# 
# Let's look at some refactoring tomorrow!
