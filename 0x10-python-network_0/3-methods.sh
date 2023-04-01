#!/bin/bash
# This script takes in a URL & displays all `HTTP` methods the server will accept.
curl -sI "$1" | awk '/Allow/{gsub(/Allow: /,"");print}'
