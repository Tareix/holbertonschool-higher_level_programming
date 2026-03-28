#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at given index
    """
    length = len(my_list)
    if length <= idx or idx < 0:
        return (my_list)

    my_list[idx] = element
    return (my_list)
