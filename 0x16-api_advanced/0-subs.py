#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'reddit_app'}
    url = f'https://www.reddit.com/r/{sys.argv[1]}/about.json'
    response = requests.get(url, headers=headers)
    data = len(response.json())
    return data
