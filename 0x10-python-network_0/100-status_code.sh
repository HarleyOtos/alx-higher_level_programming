#!/bin/bash
# A script that sends a request to URL given and display only the status code of the response. 
curl -s -o /dev/null -w "%{http_code}" "$1"
