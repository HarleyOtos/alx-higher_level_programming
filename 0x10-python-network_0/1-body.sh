#!/bin/bash
# This script takes a URL, sends a GET request to it using curl with -s mode, & displays the body of the response if the status code is 200.
curl -sI "$1" | grep "200 OK" > /dev/null && curl -sL "$1" || true
