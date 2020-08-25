# KATA THROUGH TDD - PART 2
# 
# When we left off yesterday I was trying to find a way to make the following test pass:
test.assert_equal(gtn(11), "on bir")
# This test fails, because my function currently looks like this:
def gtn(num):
    if num < 10:
	res = singles[num]
    else:
	res = tens[num]
# When passing 11, it goes to the else clause and then fails to find the key. In order to make this 
# pass I need to search one dictionary for the singles value, and the other for the tens value. So 
# how do I split an integer into its constituent parts?
# Unlike with strings or other iterables I can't take only the first position of an integer by for 
# example
ten_val = num[0]
# due to the way integers are stored in memory. I need two operations to make this happen.
# First, I can floor divide (or integer divide) the num value to get only the ten:
ten_val = num // 10
# This simply discards the difference (the single value) when dividing by ten. So how do I get that
# discarded value? We divide by 10 again but record only the difference - i.e. the modulo:
single_val = num % 10
# Now we can combine these calls into the number we need:
res = str(tens[num // 10 * 10]) + " " + str(singles[num % 10])
# So the whole function looks like this:
def gtn(num):
    if num < 10:
	res = singles[num]
    else:
	res = str(tens[num // 10]) + " " + str(singles[num % 10])
    return res
# This still fails the test, because the function is trying to find the key 11 // 10 == 1 in the 
# tens dictionary, which obviously doesn't exist. So instead of using num // 10 I have two options:
num // 10 * 10 		# returns 10 for any value 10 =< n < 20
num - (num % 10)	# returns 10 for any value 10 =< n < 20
# When passing 11 to the first value it calculates 11 // 10 == 1, then 1 * 10 == 10.
# When passing 11 to the second value it calculates 11 - (11 % 10) == 11 - 1 == 10.
# 
# I personally prefer the 2nd one but it really doesn't make much of a difference, especially given 
# how tiny this script is.
# So, new function:
def gtn(num):
    if num < 10:
	res = singles[num]
    else:
	res = str(tens[num - (num % 10)]) + " " + str(singles[num % 10])
   return res
# This passes the last test (passing 11) but not the preceeding one (passing 10), because that one 
# now resolves to "on sıfır" rather than "on": it queries the singles dictionary for key 0, finds 
# it, and adds it to the output.
# The easiest way to make this pass is check if num % 10 == 0:
def gtn(num):
    if num < 10:
	res = singles[num]
    else:
	if num % 10 == 0:
	    res = tens[num]
	else:
	    res = str(tens[num - (num % 10)]) + " " + str(singles[num % 10])
    return res
# Which passes all four tests we're now running.
# I suspect that the problem is solved now and all cases (between 0 and 99 anyway) are accounted 
# for, so let's do some refactoring. There are two if+else statements here that I would like to 
# merge, and two dictionaries where I believe one will do.
# Let's try to refactor and hit test:
def gtn(num):
    if num < 10 or num % 10 == 0:
        res = all_nums[num]
    else:
        res = str(all_nums[num - (num % 10)]) + " " + str(all_nums[num % 10])
    return res
# This passes all current tests, and I can't think of a test (passing an integer between 0 and 99, 
# remember) that will fail this code. The else clause turned into quite a long line - only one 
# position short of the Python suggested limit of 79 characters.
# One way to make this a little shorter (and get rid of that ugly num - (num % 10) business) is to 
# go back to using two dictionaries - one for units, one for tens - but number the tens with keys 
# like 1, 2, 3 instead of 10, 20, 30. In that scenario all you need is num // 10 to get the correct 
# tens key.
# I will leave this as it is, as I like having the data in a single dictionary, but for some 
# applications using two dicts (or lists, or tuples) and a shorter function may be the better 
# choice.
