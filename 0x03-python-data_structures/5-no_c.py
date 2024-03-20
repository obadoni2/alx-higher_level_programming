#!/usr/bin/python3
# 5-no_c.py

 def no_c(my_string):
     """Remove all characters c and C and c from a string."""
     copy =[x for x in my_string if x != 'c' and !='C']
     return("".join(copy))
