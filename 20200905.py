# BACK TO THE SNAKE
# 
# Right now, writing a complete static site generator is overkill. I only have two pages published 
# at the moment - it's no hardship to hand-maintain this. It will be great to be able to write an 
# update only to a template file and apply it to everything automatically, but not worth the 
# trouble of coding it right now.
# 
# Instead I'll be looking at rewriting my resume and keeping these snippets a little shorter. Let's 
# have a script I can call to generate a new Python project. It should:
# 1. Create a new folder in the current dir with the name of the project
# 2. Create files 'main.py' and 'tests.py' inside that folder
# 3. Populate the 'main.py' with a comment line that has the name of the project, and def main(): 
# 	to begin with
# 4. Populate the 'test.py' with import unittest, class tests(unittest.TestCase):, the beginnings 
# 	of the first test (something like def test... with an empty line under it) and the following:
# if __name__ == '__main__':
#     unittest.main()
# for easy calling.
# 
import os, sys

def main():
	if len(sys.argv) != 2:
		print("Please provide exactly one argument as project name")
		quit()
	else:
		project = sys.argv[1]
		try:
			os.mkdir(project)
		except:
			print("Could not create project directory: {};\nplease try again.".format(project))
			quit()
	
	mainfile = project + "/main.py"
	f = open(mainfile, "w")
	f.write("#### " + project + " ####\n\ndef main():")
	f.close()
	testfile = project + "/test.py"
	f = open(testfile, "w")
	f.write("import unittest\n\nclass tests(unittest.TestCase):\n\n    def test\n\n\n")
	f.write("if __name__ == '__main__':\n    unittest.main()")
	f.close()
	

main()
# 
# Appears to do exactly as I want. Now, let's go and finish some projects!
