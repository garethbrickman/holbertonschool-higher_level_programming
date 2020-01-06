#!/bin/bash
### Displays size of body of response from URL
curl -s "$1" | wc -c
