#!/usr/bin/python3
"""Query the Reddit API
    prints the titles of the first 10 hot posts for a subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API
    and prints the titles of the first 10 hot posts

    Args:
        subreddit (str): The name of teh subreddit

    Returns:
        Titles of the 10 hot posts or
        none if the subreddit is invalid
    """
    headers = {'User-Agent': 'RedditTopTen/1.0 (by /u/YourRedditUsername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
