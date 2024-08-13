#!/usr/bin/python3
"""This module queries the RedditAPI"""

import requests


def number_of_subscribers(subreddit):
    """Queries the RedditAPI and returns the number of subscribers
    Args:
        subreddit(str): The name of the subreddit
    Returns:
        number_of_subscribers(int): the number of subscribers
            0 if the subreddit is invalid
    """
    headers = {
        'User-Agent': 'RedditSubscriberCounter/1.0 (by /u/YourRedditUsername)'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        if response.status_code == 200:
            data = response.json()
            print(f"JSON data: {data}")
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
