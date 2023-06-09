#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    payload = {"email": email}
    response = requests.post(url, data=payload)

    print("Your email is:", email)
    print(response.text)
