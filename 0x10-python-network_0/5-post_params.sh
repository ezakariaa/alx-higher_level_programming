#!/bin/bash
#a Bash script that takes in a URL, sends a POST request to the passed URL
#and displays the body of the response

# Check if URL is passed as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Variables to send in the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send the POST request using curl and display the response body
curl -s -X POST -d "email=$email" -d "subject=$subject" "$URL"
