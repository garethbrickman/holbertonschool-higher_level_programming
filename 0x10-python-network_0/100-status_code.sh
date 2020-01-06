#!/bin/bash
### Requests URL to respond with just the response code
curl -s -o /dev/null -I -w "%{http_code}" "$@"
