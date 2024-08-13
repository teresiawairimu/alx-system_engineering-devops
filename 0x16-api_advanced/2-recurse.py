#!/usr/bin/python3
"""Recursively queries the Reddit API
returns a list containing the titles of all  hot articles for a given reddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a give reddit

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): A list containing the titles of hot articles
        after (str): the after parameter for pagination

    Returns:
        list: A list containing the titles of all hot articles
        None: if the subreddit is invalid or no results found
    """
    headers = {
        'User-Agent': 'RedditHotArticles/1.0 (by /u/YourRedditUsername)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('data', {}).get('children', [])
            for article in articles:
                hot_list.append(article.get('data', {}).get('title'))
            after = data.get('data', {}).get('after')
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
