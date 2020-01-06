#!/bin/bash
### Sends POST request with JSON file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
