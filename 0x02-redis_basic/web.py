#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import redis
import requests
reed = redis.Redis()
count = 0

def get_page(url: str) -> str:
    """returns HTML content of a URL"""
    reed.set(f"cached:{url}", count)
    r = requests.get(url)
    reed.incr(f"count:{url}")
    reed.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return r.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
