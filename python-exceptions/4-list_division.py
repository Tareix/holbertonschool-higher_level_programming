#!/usr/bin/python3
"""Module for dividing two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1: First list.
        my_list_2: Second list.
        list_length: Number of elements to process.

    Returns:
        A new list containing the division results.
    """
    new_list = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
