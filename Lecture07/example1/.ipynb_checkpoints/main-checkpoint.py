import my_module

my_module.my_function()
print(my_module.my_variable)

#my_module.my_variable = "HAM"
#my_module.my_function()

#my_module.my_module2.awesome_function()

import math
math.pi = 3
print(math.pi)

from importlib import reload
print(reload(math).pi)
print(math.pi)