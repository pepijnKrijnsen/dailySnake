# THE DEVELOPMENT CHALLENGE
# 
# I think the real challenge for a developer - almost regardless of language or
# size of project - is building something that can easily be modified.
# Building something that works is easy. Building something that works well,
# and makes efficient use of resources, and is responsive (i.e. quick), is
# harder but still very doable.
# Building something that can quickly and easily be changed and expanded is
# difficult. It's impossible to predict future requirements. If you could do
# that, you wouldn't need to design for adaptability at all: you would simply
# write the future requirements into today's code.
#
# Any website has this problem. Let's say I want to make a change to the
# navigation column. Ideally, I make that change in one place - or at most 
# two, if both HTML and CSS need to be updated - and it automatically cascades 
# to every page that includes that navigation column.
# Static site generators do this using templates. I want to do the same, but
# write the logic myself.
# 
# The basic logic is not very difficult. Consider each unique page as a 
# combination of multiple puzzle pieces. Then, create a template file for any
# piece that exists in more than one unique page.
# The top of every page, including a certain part of <head>, is the same across
# all pages. Pages may refer to different css files or have different meta
# tags, so not all of head can be used across all pages, but there's definitely
# overlap.
# Any div element can be a puzzle piece. The div containing the right hand side
# column is the same across every single page.
# The content in the left hand side column is different for every page, so that
# can never be turned into template files.
#
# Every page now becomes a sum of different elements. The homepage may be:
# document_top + open_div_column + content (not a template)
# + close_div_column + right_column.
# A blog post could be:
# document_top + unique_css_ref (this is probably only a single line) + 
# open_div_column.template + content (not a template) + close_div_column + 
# right_column.
#
# Let's see what this looks like in practice.
# 
# With the static pages - whether generated or hand-crafted - in place, let's 
# configure Bottle to serve them correctly in the next post.
