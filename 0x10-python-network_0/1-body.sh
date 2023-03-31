#!/bin/bash
# This script takes a URL, sends a GET request to it using curl with silent mode, and displays the body of the response if the status code is 200.
if [[ $(curl -s -o /dev/null -w "%{http_code}" "$1") == "200" ]]; then curl -s "$1"; fi
