#!/bin/bash
# A script that takes a URL, sends a GET request to it using curl, & displays the body of the response.
curl -s -o /dev/null -w "%{http_code}" "$1" | grep "200" > /dev/null && curl -sL "$1" || true
