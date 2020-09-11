# TESTING CHALLENGE
# 
# Some scenarios are inherently difficult to test. There are two I came across 
# recently that I'd like to explore.
# 
# 1. Tests become obsolete
# The idea behind TDD is that you start writing a test, then code, then a new 
# test, then code, ad infinitum (or until your app is finished). By the end 
# you will have a set of tests that should ALL pass.
# I wrote the following first test when writing a new bit of my bug tracker 
# app:
def testPresenterReceivesNewTicketData(self):
    self.assertEqual(main.presenter.getTicket(), "")
# 
# This very basic test just confirms that the new getTicket method I was about 
# to write exists and returns an empty string when called. This worked well 
# as a first step when I was using TDD to solve katas.
# For my next test I started to think about what that method should actually 
# do, and realised immediately that that method should receive data from the 
# View - probably in the shape of a dictionary, because JSON data and Python 
# dictionaries are basically identical - which means it would need to take at 
# least one parameter.
# The problem here is that if I redefine the getTicket method to take one 
# parameter, the first test I just wrote will always fail: the test is calling 
# the method with no parameters. In order to resolve that I would need to 
# rewrite or delete (comment out) the test.
# This is not an issue with TDD: it's an issue with the first test I 
# "automatically" wrote. The first test shouldn't call a new method with no 
# params if it's supposed to get some params. It should call the method with 
# the params it's supposed to have. If I'm not sure of the exact params yet at 
# this stage I can define a global tuple in the test suite that contains the 
# parameters, and just call the function with that tuple as the only argument. 
# I can update the tuple if new or different parameters are required across 
# all tests, if during development I realise I made a mistake.
# 
# 2. Writing tests for random values
# The ticket storage logic described above assigns a unique ID to each new 
# ticket which is a randomly generated five-digit integer starting with 2. 
# (Personal reasons.) When I tried to think of a way to test this behaviour I 
# wasn't sure how to use the assertEqual test: if I generated two random 
# numbers - one in code, one in test - the test would fail in about 9,999 out 
# of 10,000 cases.
# I could use assertRegex to check that the generated number matched the 
# format of 20000 - 29999 but that wouldn't be proof that each number was 
# unique.
# I ended up creating a .csv file from code that stored each unique ID - I 
# needed this anyway regardless of my tests, I just hadn't realised it yet 
# until I started testing - and storing each ID that was generated in that 
# file. The code - not refactored - looks like this.
def newTicket(json_data):
    f = open("lib/UIDs.csv", "r+")
    UIDs = f.read()     # reads contents of file, and sets cursor to end
    UID = str(random.randrange(20000, 29999, 1))    # wrapped in str() is 
    while UID in UIDs:      # required to make "UID in UIDs" work
        UID = str(random.randrange(20000, 29999, 1)) # ugly double code
    json_data["UID"] = UID
    f.write(UID + ",")
    f.close()
    return json_data
# 
# The return will actually not be used in finished code - this function will 
# be calling a business logic function after validating and preparing data 
# passed from the view. But for now it's useful to make the tests work while 
# the called function does not yet exist.
