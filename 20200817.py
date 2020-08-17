# BASIC RECURSION - 1
# 
# Recursion (direct recursion) refers to a function calling itself as part of the code block. It's
# an important feature of backtracking algorithms and advanced functions.
# 
# Consider the following 'normal' (non-recursive) function that takes a list of integers and
# returns a new list where each integer is 4 higher.
# 
def addFourIter(a):
    new_list = []
    for v in a:
        new_list.append(v + 4)
    return new_list

old_list = [1, 1, 2, 3, 5, 8]
print(addFourIter(old_list))
# returns [5, 5, 6, 7, 9, 12]
# 
# The following function returns the same result using recursion. Please note that while this
# demonstrates the principle of recursion, using a for loop is more efficient and easier to read
# in this case.
# 
def addFourRecur(a):
    if len(a) == 1:
        return a[0] + 4
# alternatively, the base case can be to return nothing if len(a) == 0 but that would involve one
# more recursive call
    else:
        val = a.pop() + 4   # pop the last element of the original list
        return str(addFourRecur(a)) + ", " + str(val)
# call function again with the shortened list plus the incremented last element
# note that if the recursive call and the incremented element are swapped, the list will be
# returned in reverse order        

print(addFourRecur(old_list))
# returns 5, 5, 6, 7, 9, 12
