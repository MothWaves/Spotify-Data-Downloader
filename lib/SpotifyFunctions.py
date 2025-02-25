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
    processed_entries = []
    for track_entry in tracks:
        if track_entry['track']['type'] != "track":
            raise Exception
        # Get Track Entry Data
        added_at = track_entry['added_at']
        adder_name = sp.user(track_entry['added_by']['id'])['display_name']
        added_by = {
            'display_name': adder_name,
            'id': track_entry['added_by']['id'],
            'uri': track_entry['added_by']['uri']
        }

        track = track_entry['track']
        # Get Track Data
        name = track['name']
        album = process_album(track['album'])
        artists = process_artists(track['artists'])
        disc_number = track['disc_number']
        track_number = track['track_number']
        track_id = track['id']
        uri = track['uri']

        # Put together Data
        processed_track = Track(name,
                                album,
                                artists,
                                disc_number,
                                track_number,
                                track_id,
                                uri)
        processed_entry = TrackEntry(added_at,
                                     added_by,
                                     processed_track)

        processed_entries.append(processed_entry)

    return processed_entries

def process_album(album):
    if album['type'] != "album":
        raise Exception
    name = album['name']
    album_id = album['id']
    artists = process_artists(album['artists'])
    uri = album['uri']

    return Album(name, album_id, artists, uri)

def process_artists(artists):
    processed_artists = []
    for artist in artists:
        if artist['type'] != "artist":
            raise Exception
        name = artist['name']
        artist_id = artist['id']
        uri = artist['uri']

        processed_artists.append(Artist(name, artist_id, uri))

    return processed_artists
