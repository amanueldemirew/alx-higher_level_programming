#!/usr/bin/python3
def print_list_integer(my_list=[]):
	i = len(my_list)
	for n in range(i):
		print("{:d}".format(my_list[n]))
