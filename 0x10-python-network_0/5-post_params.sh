#!/bin/bash
### Sends POST request with variables, displays body of response
curl "$@" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
