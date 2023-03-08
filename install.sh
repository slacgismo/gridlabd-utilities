#!/bin/bash
#
# gridlabd utility installer
#
# Environment
#
#   GITHUB_REPO=slacgismo/gridlabd-utilities
#	GITHUB_BRANCH=main
#

curl -sL https://rawusercontent.github.com/${GITHUB_REPO:-slacgismo/gridlabd-utilities}/${GITHUB_BRANCH:-main}/source/utility.py -o /usr/local/opt/gridlabd/current/share/utility.py
