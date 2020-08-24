# KATA THROUGH TDD
# 
# I've been learning about TDD and how it's a great thing to learn. I figured, since I barely
# have any coding experience and no real habits yet, I better get used to doing this now rather
# than having to unlearn other things when I pick it up.
# 
# I only find myself with about an hour each day to do some coding, and much of that is spent
# reading or listening. Actually writing any lines, let alone larger projects, is very rare
# right now simply because of everything else going on. Doing a simple kata allows me to
# practice some problem solving, learn a little TDD, keep the Python syntax top of mind, and
# pick up some clever tricks in the process.
# 
# Today's KATA: Turkish numbers 0-99
# Disclaimer: I'm not Turkish, I just copied this from codewars.com. Please forgive any stupid
# mistakes.
# Premise: 0-9 and multiples of ten have their distinct names. All other numbers are simply
# formed by combining the appropriate "ten"-er and 0-9, like twenty-one in English.
# 
# First test:
test.assert_equals(gtn(0), "sıfır")
# This fails, since there isn't any code. This is very easy to get to pass.
def gtn(num):
    return "sıfır"
# This is the most bone-headed, cheater, ridiculous code ever. Anyone can see that this is
# nowhere close to a resolution. THAT'S NOT THE POINT. I'm only allowed to write code that will
# make the test pass as quickly as possible.
# Next test:
test.assert_equals(gtn(1), "bir")
# Now my code fails the test again. Let's see - as long as the number being passed is less than
# 10, I only need to send a single value. So let's make a dictionary with numbers as keys, and
# the appropriate words as values.
singles = {0: "sıfır", 1: "bir" }   # etc
# and change the function to:
def gtn(num):
    return singles[num]
# Time for a new test. This code will work up to 9, so let's test for 10.
test.assert_equals(gtn(10), "on")
# Hurray, my test fails again! In order to make this pass I'll write a dictionary of multiples
# of 10 in the same fashion.
tens = { 10: "on", 20: "yirmi" }    # etc
# If I call my code again now the function will search for the key 10 in the singles
# dictionary, which obviously won't be found. I need a way to distinguish them. IF statements
# should be low down the list but there's no easy way I can think of to avoid it.
def gtn(num):
    if num < 10:
        res = singles[num]
    else:
        res = tens[num]
    return res
# Which passes the test.
# The next failing test is
test.assert_equal(gtn(11), "on bir")
# This of course fails again, because there's no key with this value in the tens dictionary
# (nor in the singles one, but that one isn't even checked because num > 10).
# 
# More fun tomorrow!
