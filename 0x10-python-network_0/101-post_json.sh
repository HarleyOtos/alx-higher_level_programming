#!/bin/bash
# A script that sends a JSON POST request to the URL passed as the first argument, & display the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
