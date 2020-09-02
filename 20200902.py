# AUTOMATING STATIC WEBSITE
# 
# So I said I would be looking into recursion again, but there's something else that I need to take 
# care of first.
# This Sunday I'll be publishing the first post in my should-be-weekly blog on family, music, and 
# tech. It has been mostly written, but I need to do two things by Sunday to make this available: 
# 1. Merge the blog (text format) into the appropriate web page (html)
# 2. Publish the whole page, as far as it's appropriate for public viewing, at Greenhost
# 
# Step one is easy to do manually for a single page, but I want to automate publishing a new blog 
# every week as soon as possible. For this I need a Python script that:
# a. Creates a new HTML file based on a pre-existing 'blog_template.html' file and a finished blog 
#   in .txt format
# b. Creates a new HTML file based on the existing /blog.html page with only a link to the latest 
#   blog added to it
# c. Deletes the current /blog.html page
# d. Uploads the new HTML file thus created to Greenhost through (s)ftp
# e. Deletes the current /blog.html file on Greenhost's side and uploads the new version
# 
# I will be doing some reading and light testing today about how to use Greenhost's (s)ftp feature 
# to update an existing site, and create the required directory structure (probably very basic for 
# now) in our existing domain.
# 
# In order to complete step 2 above, I'll need to make sure the whole page is fit for public 
# access. This will involve creating a carbon copy of the current website project and deleting 
# everything that is not yet ready - links to my resume, my bio, my portfolio, etc. For the moment 
# it will just be a blog with some extra bits, with an update once a week, while I work on the 
# website itself and on my portfolio apps in the background.
# 
# I can't yet write the Python script that handles communication with Greenhost, as I need to read 
# up on using FTP for this purpose. However, I can start on the bit that creates new HTML pages 
# from existing template pages plus completed blog files.
# 
# What I'm thinking right now is to read a template .html UP TO the part where the blog needs to 
# go - read the blog file and append that - then read the rest of the template .html.
# 
def main():
    content_dir = "path/to/content/"
    content_file = "path/to/content/*.txt"
    # check that there's only one file in ~/projects/blog/completed/
    if len(os.listdir(content_dir)) != 1:
        print("Please limit number of files to 1")
        quit()
    # read that file into a variable and close it
    f = open(content_file)
    blog = f.read()
    f.close()
    # read both halves of the blog post template into separate variables
    template_file = "/path/to/template.html"
    f = open(template_file)
    line = ""
    template_top = ""
    template_bottom = ""
    while "START blog" not in line:
        line = f.readline()
        template_top += line
    while "END blog" not in line:
        line = f.readline()
    template_bottom = f.read()
    f.close()
    # generate a complete blog page
    new_blog = template_top + blog + template_bottom
# 
# So far so good! More tomorrow.
