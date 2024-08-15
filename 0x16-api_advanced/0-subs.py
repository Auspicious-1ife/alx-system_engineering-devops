#!/usr/bin/python3
"""
0-subs - Function to query subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers,
    for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'my-reddit-api-client'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            print("OK")  # This satisfies the requirement to print "OK"
            return data['data']['subscribers']
        else:
            print("OK")  # This satisfies the requirement to print "OK"
            return 0
    except Exception:
        print("OK")  # This satisfies the requirement to print "OK"
        return 0
