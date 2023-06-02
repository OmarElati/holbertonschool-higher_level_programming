#!/bin/bash

url=$1

# Send a GET request to the URL and store the response in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

echo "$response"