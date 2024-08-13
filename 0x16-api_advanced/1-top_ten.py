#!/usr/bin/python3
"""
2-recurse - Recursively fetch all hot articles from a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to get all hot article titles
    from the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulates the titles of hot articles.

    Returns:
        list: List of all hot article titles or None if subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'my-reddit-api-client'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                hot_list.extend(post['data']['title'] for post in posts)
                next_after = data.get('data', {}).get('after', None)
                if next_after:
                    return recurse(subreddit, hot_list)
                else:
                    return hot_list
            return hot_list
        return None
    except Exception:
        return None
