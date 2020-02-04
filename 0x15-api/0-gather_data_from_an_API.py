#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list progress
# from REST API at https://jsonplaceholder.typicode.com/

import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(argv[1])).json()
    done = []
    for task in tasks:
        if task['completed'] == True:
            done.append(task)
    print("Employee {} is done with tasks({}/{}):"
          .format(user['name'], len(done), len(tasks)))