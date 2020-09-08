# SHIT HAPPENS
# 
# So, slight issue with yesterday's post: I forgot to return anything from my routed functions.
# This is what happens when you don't test, people!
# Anyway. Here's the folder structure for my portfolio site:
# website/
#   index.html
#   blog.html
#   bio.html
#   resume.html
#   blog/
#     <all_blogposts.html>
#   css/
#     style_main.css
#     style_blog.css
#     style_portfolio.css
#   files/
#     <various images and downloads>
# 
# That's really all there is to it. Let's build some routes - properly this time - to serve these 
# static files through a Bottle script.
from bottle import Bottle, run, static_file
import os

parent = os.path.dirname(os.path.abspath(__file__))
parent += "/website"

app = Bottle()

@app.route("/")
def serve_home():
    return static_file("index.html", root = parent)

run(app, host = "localhost", port = 8080, debug = True)
# 
# This returns index.html for the domain.com root.
@app.route("<filename:re:.*\.css>")
def css(filename):
    return static_file(filename, root = parent)
# 
# Returns any css file called by name - either from a page or by the user, should they so wish.
@app.route("<filename:re:.*.\.html>")
def static_html(filename):
    return static_file(filename, root = parent)
# 
# Returns any .html file whose name matches the name in the URL; domain.com/resume returns 
# root/resume.html, domain.com/blog/f1rstp0st returns root/blog/f1rstp0st.html, etc.
