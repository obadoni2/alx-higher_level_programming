#!/bin/bash
# display all HTTP method acceptable by server
curl -sI $1 | grep Allow | cut -d '' -f2-