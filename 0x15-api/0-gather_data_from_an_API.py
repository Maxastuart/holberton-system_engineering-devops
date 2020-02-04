#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list progress
# from REST API at https://jsonplaceholder.typicode.com/

import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
              .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos').json()

    print("Employee {} is done with tasks({}/{}):".format(user['name'], done, total))
