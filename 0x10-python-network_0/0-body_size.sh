#!/bin/bash
# Script that takes a URL and counts the body size
curl -s "$1" | wc -c
