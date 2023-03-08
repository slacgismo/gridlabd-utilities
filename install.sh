#!/bin/bash
#
# gridlabd utility installer
#

GITHUB_REPO=slacgismo/gridlabd-utilities

if [ $# -eq 0 ]; then
	echo "./install.sh NAME"
fi

curl -sL https://rawusercontent.github.com/$GITHUB_REPO/main/source/$1.py -o /usr/local/opt/gridlabd/current/share/$1.py
