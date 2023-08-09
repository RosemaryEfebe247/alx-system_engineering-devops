#!/usr/bin/python3
"""Function that returns the total no of Reddit subscribers
    return 0 if no subreddit is passed
    """
import requests


def number_of_subscribers(subreddit):
    """Connecting to the Reddit url to get the total sub."""

    headers = {'User-Agent': 'reddit_app'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        err = response.raise_for_status()
    except Exception as err:
        return (0)
    return subscribers
