#!/usr/bin/python3
"""print a header of a response from a URL."""
import sys
import requests


if __name__ == '__main__':
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
