#!/usr/bin/python3
def print_list_integer(my_list = []):
    for i in range(len(my_list)):
        if type(my_list[i]) == int:
            print("{}".format(my_list[i]))
print_list_integer([1, "cahid", 3, 4, 5])
