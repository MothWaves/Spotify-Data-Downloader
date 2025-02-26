#!/usr/bin/env python3

from lib.SpotifyClasses import *
from lib.Singletons import *
import json

def get_tracks(sp, pl_id):
    requests_counter = RequestsCounter()
    requests_counter.check_rate()
    # Request playlist tracks
    results = sp.playlist_items(pl_id)
    requests_counter.increment()
    tracks_results = results['items']
    while results['next']:
        # Waits a bit to not hit the spotify api rate limit.
        requests_counter.check_rate()
        results = sp.next(results)
        tracks_results.extend(results['items'])
        requests_counter.increment()

    return process_track_entries(tracks_results)

def process_owner(owner):
    # Checks if type of data is user
    if owner['type'] != 'user':
        raise Exception

    # Creates User
    name = owner['display_name']
    user_id = owner['id']
    uri = owner['uri']
    return User(name, user_id, uri)

def process_track_entries(tracks):
    added_by_list = AddedByIdList()
    processed_entries = []
    for track_entry in tracks:
        # Get Track Entry Data
        added_at = track_entry['added_at']
        if track_entry['added_by']['id'] not in added_by_lists.ids:
            added_by_list.ids.append(track_entry['added_by']['id'])
        added_by = {
            # display name will be added later.
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
    return processed_track

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
