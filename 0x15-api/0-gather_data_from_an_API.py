#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list progress.
# from REST API at https://jsonplaceholder.typicode.com/

import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    print(r.json())
