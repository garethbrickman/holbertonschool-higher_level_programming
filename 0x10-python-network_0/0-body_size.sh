#!/bin/bash
### Displays size of body of response from URL | curl -s "$@" | grep -i Content-Length | awk '{print $2}'
curl -s "$1" | wc -c
