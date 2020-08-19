# THE OS MODULE
# 
# Python can use the os module to use OS specific methods and get OS specific attributes. The # module is built in to Python and does not need to be installed - you only need to import it:
import os
# A full description of the module including all methods and attributes can be found in the Python # docs: https://docs.python.org/3/library/os.html
# The OS module is required for several common automation actions, including (but not limited to):
# 1. Getting details about the OS
# 2. Renaming, moving, or deleting files & directories
# 3. Copying or creating directories
# 4. Executing shell commands
# 5. Getting process IDs
# 
# Note that copying or creating files (not directories) can be handled with Python's built-in 
# open() function.
# 
# One more feature that is useful for certain automation tasks is to give Python access to # arguments passed when calling the script. In other words, if I have a script called backup.py # that copies any file provided to it to the ~/backups directory, you can use the sys.argv() # method.
# This method is part of the sys module, so first we need to...
import sys
# Now we can access any arguments passed to our Python script through sys.argv(). This method # returns a list where index0 is the name of the script itself and any subsequent indices are # arguments passed to the script.
# For example: if I want to backup my photo.jpg using this script, I can call
backup.py photo.jpg
# ...and the list returned by sys.argv() now contains:
['backup.py', 'photo.jpg']
