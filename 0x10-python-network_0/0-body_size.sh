#!/bin/bash
### Displays size of body of response from URL
curl -si "28c56b31c5e1@28c56b31c5e1.20.hbtn-cod.io" | grep "Content-Length:" | cut -d ":" -f2
