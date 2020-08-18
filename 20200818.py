# WORKING WITH FILES
# 
# Python is a great automation/scripting language. Working with files is an important part of 
# automation.
# If you need to move, copy, or delete files, you will need to import the required methods for 
# your operating system using "import os" at the start of your script. However, Python has a 
# built-in function for creating, writing, appending to, and reading files: open()
# 
# This function takes two parameters: filename (required), mode (default "rt" for "read", "text")
# Other modes are "a" for Append (add to an existing file - create file if it doesn't exist), "w" 
# for Write (overwrite an existing file - is created if it doesn't exist) or "x" for Create 
# (create # a new file - raises an error if it exists).
# Instead of "t" for text you can specify "b" for binary when working with non-text files.
# 
# The open() function returns a file object that Python can interact with. This object has two 
# major (and very self-explanatory) methods: read() and write().
# The read() method can read the contents of a file object created with a call to open(). 
# Alternatives of this method include readline(), readlines(), and seek(). The latter can be 
# useful to reset the read operation you did earlier: reading from a file moves the "needle". In 
# other words, if you call read() on a file object to return all contents of the file and then 
# call read() again on the same object, the second call will return an empty string.
# The write() method handles writing to a file. The exact behaviour of the write() method depends
# on the mode in which the file was opened in the first place:
# 1. If the open() call had "a" (or "ab" for binary) as its second parameter, the write() method 
# appends new content to the end of the file.
# 2. If the open() call had "w" (or "wb") as its second parameter, the write() method overwrites 
# any existing content of the file.
# 
# Next update will go deeper into the various scenarios where various file object methods come 
# into play.
