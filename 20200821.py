# USING OPEN() TO WRITE FILES
# 
# Again, we'll be dealing with text type files ONLY.
# Writing a file - either an existing file or a new file - can be done in two modes:
# 1. Write, which overwrites any pre-existing content of the file
# 2. Append, which adds data to the end of a file
# 
# Let's create a new file, making sure that it does not already exist:
open("new_page.html", "x")
# 
# Now let's write open this new file in Write mode to add some data:
mfo = open("new_page.html", "w")
# 
# ...and write some data to it:
mfo.write("<!DOCTYPE html>")
# 
# We now realise that this html file is slightly useless: it defines the doctype and doesn't do 
# anything else. I want to add some more data. I can do that, because the file has not been closed 
# in the meantime. Multiple write() calls to the same file object - that is to say, the object 
# created by one open() call - append to each other.
mfo.write("\n<html>\n<body>\n<h1>Hello, world!</h1>\n</body>\n</html>")
# I'm adding linebreaks to make the file easier to read if I open it in a text editor. If this is a 
# file that will only be rendered, and you don't need to look at it, you can leave the linebreaks 
# out since HTML doesn't render newline characters.
# If I now open the file in a text editor - or call mfo.close(), then mfo = open("new_page.html"), 
# then print(mfo.read()) - it will look like this:
<!DOCTYPE html>
<html>
<body>
<h1>Hello, world!</h1>
</body>
</html>
# Which, if opened with a browser, would display a web page - albeit a very basic one.
# Keep in mind to always call <fileobject>.close() after you finish working with a file. This frees 
# up the memory that was used to store the file object. Also note that if you call open() with "w" 
# as the second argument, any writes you do to the file will overwrite what's there. If you need to 
# add content to a file you have not yet called open() on, make sure to use "a" for Append as the 
# second parameter.
# Two final words of warning: trying to call write() on a file opened in read mode, or calling 
# read() on a file opened in write or append mode, will return an io error (unsupported operation). 
# Calling open() with "w" on a file that was already opened will overwrite that file with nothing, 
# effectively deleting the contents of the file completely.
# Opening an already open file with "a" does not have this effect, but it's still better to close 
# the file after reading or writing is completed for that particular code block.
# Calling open() with "r" (or nothing) as the 2nd parameter on a file that is already open does not 
# impact the file itself, but it also doesn't allow you to read the file contents - calling read() 
# on the file object returns an empty string.
