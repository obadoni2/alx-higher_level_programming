#!/bin/bash
#sends a req to URL and display size of response

cur -so/dev/null  -w '%{size_download}\n' $1
