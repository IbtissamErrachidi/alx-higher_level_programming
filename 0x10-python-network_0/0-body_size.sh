#!/bin/bash
# Bash script to get the body size of a request
size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')
echo "Size of the body: $size bytes"

