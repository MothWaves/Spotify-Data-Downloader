#!/usr/bin/env python3

import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-private,playlist-read-collaborative"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playlists()
playlists = results['items']
while results['next']:
    results = sp.next(results)
    playlists.extend(results['items'])

print(json.dumps(playlists))
