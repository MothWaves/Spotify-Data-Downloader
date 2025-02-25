#!/usr/bin/env python3

from lib.SpotifyClasses import *
import json

def get_tracks(sp, pl_id):
    # Request playlist tracks
    results = sp.playlist_items(pl_id)
    tracks_results = results['items']
    while results['next']:
        results = sp.next(results)
        tracks_results.extend(results['items'])

    return process_track_entries(sp, tracks_results)

def process_owner(owner):
    # Checks if type of data is user
    if owner['type'] != 'user':
        raise Exception

    # Creates User
    name = owner['display_name']
    user_id = owner['id']
    uri = owner['uri']
    return User(name, user_id, uri)

def process_track_entries(sp, tracks):
    processed_entries = []
    for track_entry in tracks:
        # Get Track Entry Data
        added_at = track_entry['added_at']
        adder_name = sp.user(track_entry['added_by']['id'])['display_name']
        added_by = {
            'display_name': adder_name,
            'id': track_entry['added_by']['id'],
            'uri': track_entry['added_by']['uri']
        }

        # Check type of playlist entry
        if track_entry['track']['type'] == "track":
            processed_content = process_tracks(track_entry['track'])
        elif track_entry['track']['type'] == "episode":
            processed_content = process_episodes(track_entry['track'])
        else:
            raise Exception

        processed_entry = TrackEntry(added_at,
                                     added_by,
                                     processed_content)

        processed_entries.append(processed_entry)

    return processed_entries

def process_tracks(track):
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

def process_episodes(episode):
    name = episode['name']
    description = episode['description']
    show = process_show(episode['show'])
    episode_id = episode['id']
    uri = episode['uri']

    return Episode(name, description, show, episode_id, uri)

def process_show(show):
    name = show['name']
    description = show['description']
    publisher = show['publisher']
    show_id = show['id']
    uri = show['uri']

    return Show(name, description, publisher, show_id, uri)

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
