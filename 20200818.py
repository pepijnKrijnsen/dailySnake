# WORKING WITH FILES
# 
# Python is a great automation/scripting language. Working with files is an important part of 
# automation.
# Working with files is done through the open() function. This function takes two parameters:
# filename (required), mode (default "rt" for "read", "text")
# Other modes are "a" for Append (add to an existing file - create file if it doesn't exist), "w"
# for Write (overwrite an existing file - is created if it doesn't exist) or "x" for Create (create # a new file - raises an error if it exists).
# Instead of "t" for text you can specify "b" for binary when working with non-text files.
# 
# Let's create a new file:
open("newfile.txt", "x")
# Since this is a text file, I don't need to specify "t" as the third param. We should now have an # empty file called "newfile.txt" in our script's directory.

The open() function returns a file object that Python can interact with. This object has two major (and very self-explanatory) methods: read() and write().
The read() method can read the contents of a file object created with a call to open(). By default it reads the contents of the whole file into memory. If you want to limit how much of a file is read, you have two options:
1. Pass an integer value as a parameter to the read() method, as in fileObject.read(10), to only read that many characters from the start of the file;
2. Use the readline() method instead, which reads each line one by one, as in fileObject.readline(). Using readline moves the 'needle', so calling readline() twice on the same file object returns the first and second line of that object.

The write() method handles writing to a file. The exact behaviour of the write() method depends on the mode in which the file was opened in the first place:
1. If the open() call had "a" (or "ab") as its second parameter, the write() method appends new content to the end of the file.
2. If the open() call had "w" (or "wb") as its second parameter, the write() method overwrites any existing content of the file.
