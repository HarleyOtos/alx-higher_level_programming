#!/bin/bash
# A script that takes a URL, sends a GET request to it using curl, & displays the body of the response.
curl -sI "$1" | grep "200 OK" > /dev/null && curl -sL "$1" || true
