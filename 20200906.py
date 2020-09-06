# PUT A STOPPER ON DEV
# 
# Little Harry Potter reference there.
# 
# It's funny because this is about Bottle! Get it? Put a stopper on... ah 
# forget it.
# 
# Bottle is a very small web framework with built-in development server and 
# templating engine. It does the tricky HTTP request and response parts 
# without getting in the way, which is perfect for what I'm trying to use it 
# for right now.
# 
# Let's have some code:
from bottle import Bottle, run

app = Bottle()

@app.route("/hello")
dev home():
    return "Hello, world!"

run(host = "localhost", port = 8080)
# 
# The above is technically dynamic, because a web page is generated based on a 
# user's request - albeit an extremely basic one. However, nothing ever 
# changes in the world of Hello - there's nothing a user can do to trigger a 
# different response from the server - so it's very static, too.
# 
# Bottle can use dynamic URLs, like so (extending the above a little):
from bottle import template

@app.route("/hello/<name>")
def greet(name = "Stranger"):
    return template("What's the story, {{name}}?", name = name)
# 
# calling /hello/peppy will return "What's the story, peppy?"
# Instead of using the route decorator, the request methods get, post, put, 
# delete and patch can be used instead. Route defaults to get, if none are 
# specified. This makes it very easy to work with forms and pass data between 
# the user and the app.
# 
# Finally, static files can be served using the static_file method. These may 
# include things like images or css files that are used by dynamically 
# rendered pages, but can also be static pages that are served as part of an 
# otherwise dynamic website.
from bottle import static_file

@route("/files/<filename>")
def static(filename):
    return static_file(filename, root="/abs/path/to/dir/")
# 
# This route will find any file with name <filename> that exists in the files/ 
# directory. A page (regardless of whether it's static or dynamic) that links 
# to a css file can href="/files/layout.css" will be served the file with that 
# name in the files/ dir; a page that includes an img with src="/files/go.png"
# will include the file with that name.
# The static_file method can also be used to serve full static html pages in 
# the same fashion. Assuming that my homepage is actually a static web page 
# and most of the other pages of my site are at that root:
@route("/")
def static_page():
    return static_file("index.html", root="/abs/path/to/dir")
# 
# My main next problem - after I learn all the Bottle ins and outs, but the 
# documentation is actually good so that shouldn't be a big deal - is getting 
# to know the built-in template engine and using it to easily generate and re-
# generate static pages.
