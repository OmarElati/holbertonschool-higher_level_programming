#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
url=$1
header_name="X-School-User-Id"
header_value=98
response=$(curl -sX GET -H "$header_name: $header_value" "$url")
echo "$response"
