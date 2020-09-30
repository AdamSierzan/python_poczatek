# We want to use functions from Packages_and_modules functions

import hello

# Witha a "." we can call the function and variables in "hello"

hello.say_hello()
name = input("What's your name")
hello.say_hello_with_name(name)

# Python is looking for a module, then he saves the information about it
# then he loads it and let us use it

# First it checks the list of previosly loaded modules
# Then he checks the library
# Then the catalog
# And then localization in PythonPath
# THen he checks installed undefault libraries

# If we would like to use welcome.py script in different
# script, not directly but from other destination
# we have to create catalog and import it to our python path
