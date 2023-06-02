#!/bin/bash
# Send a GET request to the URL and store the response in a variable
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
