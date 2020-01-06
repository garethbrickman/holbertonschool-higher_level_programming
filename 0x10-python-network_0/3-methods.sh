#!/bin/bash
### Displays all HTTP methods server will accept
curl "$@" -sI | grep -i "Allow" | cut -d " " -f 2-
