#!/usr/bin/env python3

import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

from lib.SpotifyFunctions import *
from lib.SpotifyClasses import *

scope = "playlist-read-private,playlist-read-collaborative"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get current_user id
current_user_id = sp.current_user()['id']

# Get Playlists
results = sp.current_user_playlists()
playlists_result = results['items']
while results['next']:
    results = sp.next(results)
    playlists_result.extend(results['items'])

# Process Playlists
my_playlists = []
others_playlists = []
counter = 1
for playlist in playlists_result:
    if playlist['type'] != "playlist":
        raise Exception
    # Get Playlist Data
    title = playlist['name']
    description = playlist['description']
    owner = process_owner(playlist['owner'])
    pl_id = playlist['id']
    pl_snapshot_id = playlist['snapshot_id']
    uri = playlist['uri']
    processed_pl = Playlist(title, description, owner, pl_id, pl_snapshot_id, uri)

    # Gather tracks for playlist
    processed_pl['track_entries'] = get_tracks(sp, pl_id)

    # Split into current_user's playlists and other's playlists
    if owner['user_id'] == current_user_id:
        my_playlists.append(processed_pl)
    else:
        others_playlists.append(processed_pl)
    print("Playlist " + str(counter) + " Done")
    counter += 1
    print(json.dumps(processed_pl))
    exit(0)

print(json.dumps(my_playlists))
