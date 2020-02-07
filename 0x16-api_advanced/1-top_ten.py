#!/usr/bin/python3
# Defines top_ten function

import requests as r


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/hot?count=10'.format(subreddit),
                  headers={'user-agent': 'python:v3.5.2 (by /u/maxastuart)'}
                  )
        g.raise_for_status()
        for i in range(10):
            print(g.json().get('data').get('children')[i].get('data')
                  .get('title'))
    except Exception as e:
        print('None')
