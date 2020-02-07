#!/usr/bin/python3
# Defines number_of_subscribers function

import requests as r


def number_of_subscribers(subreddit):
    """
    queries the Reddit API for a subreddit's number of active subscribers.

    return(int): number of subreddit's subscribers, 0 if subreddit invalid
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/about'.format(subreddit),
                  headers={'user-agent': 'python:v3.5.2 (by /u/maxastuart)'}
                  )
        g.raise_for_status()
        return g.json().get('data').get('subscribers')
    except Exception as e:
        return 0
