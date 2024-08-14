#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'myRedditApp/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for redirect status
        if response.status_code == 302:
            return 0
        
        # Check for successful response
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        
        # If the response code is not 200 or 302, return 0
        return 0
    
    except requests.RequestException:
        # Catch any exceptions related to the request
        return 0

