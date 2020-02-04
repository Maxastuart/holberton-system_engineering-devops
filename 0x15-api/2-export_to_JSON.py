#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list

import json
import requests as r
from sys import argv
if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users/{}'
                 .format(argv[1])).json()
    tasks = r.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                  .format(argv[1])).json()

    with open('{}.json'.format(argv[1]), mode='w') as f:
        json.dumps(argv[1] + ":", tasks)
