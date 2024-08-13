#!/usr/bin/python3
"""Recursively queries the Reddit API,
parses teh titles of all hot articles,
and count given keywords"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursively queries the Reddit API, parses the titles of all
    hot articles, and counts given keywords

    Args:
        subreddit (str): the name of the subreddit
        word_list (list): a list of keywords to count
        after (str): The 'after' parameter for pagination
        word_count (dict): a dictionary to store the count of each keyword

    Returns:
        Prints the sorted count of keywords
    """
    headers = {
        'User-Agent': 'RedditKeywordCounter/1.0 (by /u/YourRedditUsername)'}
    url = f"https://ww.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json()
        articles = data.get('data', {}).get('children', [])
        for article in articles:
            title = article.get('data', {}).get('title', '').lower(). split()
            for word in title:
                if word in word_count:
                    word_count[word] += 1
        after = data.get('data', {}).get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return
    except requests.RequestException:
        return None
