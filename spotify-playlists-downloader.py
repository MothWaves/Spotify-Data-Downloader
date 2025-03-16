#!/usr/bin/env python3

import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

from lib.SpotifyFunctions import *
from lib.SpotifyClasses import *
from lib.Singletons import *
import os
import sys
from pathlib import Path

if sys.platform != "linux":
    print("Linux is the only implemented os, thus far.")
    exit(-1)

scope = "playlist-read-private,playlist-read-collaborative,user-library-read"
requests_counter = RequestsCounter()
sp = SpotifySingleton(spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope),retries=10,requests_timeout=20))

# Get current_user id
current_user = sp.current_user()
requests_counter.increment()
current_user_id = current_user['id']
current_user_uri = current_user['uri']

# TODO Load existing playlists from json files.

# Get Playlists
results = sp.current_user_playlists()
requests_counter.increment()
playlists_result = results['items']
while results['next']:
    requests_counter.check_rate()
    results = sp.next(results)
    requests_counter.increment()
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

results = sp.current_user_saved_tracks()
requests_counter.increment()
tracks_results = results['items']
while results['next']:
    requests_counter.check_rate()
    results = sp.next(results)
    requests_counter.increment()
    tracks_results.extend(results['items'])

liked_songs = process_track_entries(tracks_results)

# Get names of added_by ids.
added_by_list = AddedByList()
added_by_list.get_display_names()

add_display_names(others_playlists)
# Ok so you don't really need to do much thinking for these playlists
# because all of the track entries here will be added by you
# unless its a collaborative playlist but even that
# doesnt apply to the liked songs.
# But whatever. Easier to use the existing function than to just side-step the issue.
# Ok, update, due to the fact liked_songs is structured
# differently I can't use add_display_names either way
# so I guess it all works out in the end and the function
# is only used when necessary.
add_display_names(my_playlists)
for track in liked_songs:
    track['added_by'] = {}
    track['added_by']['display_name'] =  added_by_list.display_names[current_user_id]
    track['added_by']['id'] =  current_user_id
    track['added_by']['uri'] =  current_user_uri

# Create directory for playlists if it doesn't exist.
dir_path = Path('./spotify-playlists')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

others_playlists_p = dir_path / "others_playlists.json"
my_playlists_p = dir_path / "my_playlists.json"
liked_songs_p = dir_path / "liked_songs.json"

# Write data to files.
with open(others_playlists_p, "w") as f:
    json.dump(others_playlists, f, indent="\t")
with open(my_playlists_p, "w") as f:
    json.dump(my_playlists, f, indent="\t")
with open(liked_songs_p, "w") as f:
    json.dump(liked_songs, f, indent="\t")
