#!/bin/bash
# A script that takes a URL, sends a GET request to it using curl, & displays the body of the response.
curl -sL -w "%{http_code}" "$1" | awk '$NF == 200 {getline; print}'
