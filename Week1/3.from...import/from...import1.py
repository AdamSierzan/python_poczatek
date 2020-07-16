# # PEP8 says that it's the best to divide import into 3 ggroups
# # 1) import from standard library
# # 2) import from outiside libraries
# # 3) import from our own code
# # *We don't have to worry about manual importing of codes
# # We can use optimize imports function (in pycharm)

# # # Dangerous import!
# # When using:
# # from "whatever" import *
# # we import all elements form module
# # We have to watch out because we can easily loose 
# # control over imported packages

# # We can use underscore "_", then python wont import it


# # Import as, lets us import something as something else
# from "something" import " something" as "something"

# # If we are in the same package (folder) as the other files
# # we can use 
# # It's called relative import
# from . import "something"

# # We have to remember three thing:
# It only works with from . import "something"