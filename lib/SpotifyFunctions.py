#!/usr/bin/env python3

from lib.SpotifyClasses import User
from lib.SpotifyClasses import Track
import json

def get_tracks(sp, pl_id):
    # Request playlist tracks
    results = sp.playlist_items(pl_id)
    tracks_results = results['items']
    while results['next']:
        results = sp.next(results)
        tracks_results.extend(results['items'])

    return process_tracks(sp, tracks_results)

def process_owner(owner):
    # Checks if type of data is user
    if owner['type'] != 'user':
        raise Exception

    # Creates User
    name = owner['display_name']
    user_id = owner['id']
    uri = owner['uri']
    return User(name, user_id, uri)

def process_tracks(sp, tracks):
    for track in tracks:
        # Get Track Entry Data
        added_at = track['added_at']
        sp.
        added_by =

        # Get Track Data
