#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage
usage() {
    echo "Usage: $0 <challenge_code>"
    echo "Provide the challenge code as a parameter."
    echo "Example: $0 784019874562340ghjsfdk"
    exit 1
}

# Check if the challenge code is provided
if [ "$#" -ne 1 ]; then
    usage
fi

CHALLENGE_CODE="$1"

echo "Possible keys:"

# macOS uses 'md5', Linux typically uses 'md5sum'
if command -v md5 >/dev/null 2>&1; then
    printf "%sNetGuard3" "$CHALLENGE_CODE" | md5
    printf "%sNetGuard2" "$CHALLENGE_CODE" | md5
elif command -v md5sum >/dev/null 2>&1; then
    printf "%sNetGuard3" "$CHALLENGE_CODE" | md5sum | awk '{print $1}'
    printf "%sNetGuard2" "$CHALLENGE_CODE" | md5sum | awk '{print $1}'
else
    echo "Error: Neither 'md5' nor 'md5sum' command was found." >&2
    exit 1
fi
