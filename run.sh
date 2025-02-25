#!/usr/bin/env sh

# This script is made around my own private setup for this program and will not work without changes.
# You can use it as a starting off point, though.

# Activates python virtual environment
source .virtual-env/bin/activate
# Sets env variables.
source ./set-env-variables.sh
# Runs program
python spotify-playlists-downloader.py
# Moves to export folder
cd ./spotify-playlists
# Git commit
git init .
date_var="$(date -Iminutes)"
git add .
git commit -m "Download Spotify Playlists ($date_var)"
