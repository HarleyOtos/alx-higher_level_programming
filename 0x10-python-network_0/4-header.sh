#!/bin/bash
# A script that takes a URL as an argument, sends a GET request to the URL with a custom header, and displays the response.
curl -sH "X-School-User-Id: 98" "$1"
