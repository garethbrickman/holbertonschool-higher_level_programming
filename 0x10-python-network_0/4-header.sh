#!/bin/bash
### Sends GET request with header variable, displays body of response
curl "$@" -sX GET -H "X-HolbertonSchool-User-Id: 98"
