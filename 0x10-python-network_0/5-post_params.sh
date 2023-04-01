#!/bin/bash
# A script that takes a URL, sends a POST request to it using `curl` with silent mode, and displays the body of the response.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
