#!/usr/bin/python3

from sys import argv


if len(argv) > 1:
    url = "http://www.google.com/"+argv[1]
    print(url)
else:
    print("no args")
