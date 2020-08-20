# USING OPEN() TO READ FILES
# 
# NOTE: We'll be dealing exclusively with text files, not binary files.
# ALSO NOTE: This does not only mean files with a .txt extension - it includes any file that 
# consists exclusively of text, such as source code (.py, .html), data transfer formats (.xml, 
# .json), even .csv files provided they were not tainted by Excel.
# 
# The open() method always returns a file object. If you're using open() to explicitly create new 
# files, it can be called without having to capture the object that's returned. When calling open() 
# for reading, appending, writing, or updating a file, you do need to capture the file object so 
# you can interact with it.
# Let's assume we have a file called template.html in the same directory as the script. We want to 
# read the contents of that file.
template_file = open("template.html")
# 
# Now we have a variable 'template_file' that contains the contents of the file 'template.html'. 
# The default mode for the open() method is read, which is why we did not specify a second argument 
# when we called it.
# There are three common methods to call on the file object, and a small number of less common 
# methods that are nonetheless useful.
print(template_file.read())
# prints all contents of the file to console - any newline characters in the file are retained, if 
# the html file we opened looks like this:
<html>
</html>
# The information printed to console looks like this:
<html>
</html>
# The other two common methods for reading are readline() to return one line, and readlines() to 
# return a list of all lines.
# Both read() and readline() accept a single integer parameter to specify how much of the file or 
# line to read. The default is -1 which indicates the entire file (in case of read) or line (in 
# case of readline).
# All three methods - read, readline, and readlines - move the seek position in the file. This is 
# to say, if you call read() on a given file, the entire file will be read and the seek position 
# will now be at the end of the file. Calling read() again on the same file will return an empty 
# string.
# The tell() method returns the current position of the string in the file. The seek() method 
# places the seeker at the byte passed when calling seek() - i.e., calling fileObject.seek(0) 
# returns the seeker to the start of the file.
