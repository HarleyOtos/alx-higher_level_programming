#!/usr/bin/env python3
"""Sends a POST request to passed URL with an email as a parameter to
the specified URL and displays the response body
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
