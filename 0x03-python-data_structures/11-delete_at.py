#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete and itrm at specific position in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
        returm(my_list)
