#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

response=$(curl -sX POST -d "email=$email" -d "subject=$subject" "$url")

echo "POST params:"
echo "    email: $email"
echo "    subject: $subject"
echo "$response"

