#!/usr/bin/python3
# Defines recurse function

import requests as r


def recurse(subreddit, hot_list=[]):
    """
    queries the Reddit API for the titles of all a subreddit's hot articles

    return: List of the titles, or None if none
    """
    count = len(hot_list)
    print(count)
    g = r.get('https://api.reddit.com/r/{}/hot'
              .format(subreddit), headers={
                  'user-agent': 'python:v3.5.2 (by /u/maxastuart)'},
              params={'count': count, 'limit': 1})
    if g.raise_for_status() is None:
        t = g.json().get('data').get('children')[0].get('data').get('title')
        print(t)
        hot_list += t
        return recurse(subreddit, hot_list)
    else:
        return None
