#!/usr/bin/python3
"""Function to print first 10 hot post
"""
import requests


def top_ten(subreddit):
    """Links to reddit to print top 10 hot posts"""
    headers = {'User-Agent': 'reddit_app'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    try:
        response = requests.get(url, headers=headers)
        err = response.raise_for_status()
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:
            title = post['data']['title']
            print(title)
    except Exception as err:
        print('None')
