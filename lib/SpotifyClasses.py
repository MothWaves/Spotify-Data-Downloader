#!/usr/bin/env python3

class Playlist:
    track_entries = []
    def __init__(self, title, description, owner, pl_id, pl_snapshot_id, uri):
        self.title = title
        self.description = description
        self.owner = owner
        self.pl_id = pl_id
        self.pl_snapshot_id = pl_snapshot_id
        self.uri = uri

class TrackEntry:
    def __init__(self, added_at, added_by, track):
        self.added_at = added_at
        self.added_by = added_by
        self.track = track
class Track:
    def __init__(self, name, album, artists, disc_number, track_number, track_id, uri):
        self.name = name
        self.album = album
        self.artists = artists
        self.disc_number = disc_number
        self.track_number = track_number
        self.track_id = track_id
        self.uri = uri
class Episode:
    def __init__(self, name, description, show, episode_id, uri):
        self.name = name
        self.description = description
        self.show = show
        self.episode_id = episode_id
        self.uri = uri
class Show:
    def __init__(self, name, description, publisher, show_id, uri):
        self.name = name
        self.description = description
        self.publisher = publisher
        self.show_id = show_id
        self.uri = uri
class Album:
    def __init__(self, name, album_id, artists, uri):
        self.name = name
        self.album_id = album_id
        self.artists = artists
        self.uri = uri
class Artist:
    def __init__(self, name, artist_id, uri):
        self.name = name
        self.artist_id = artist_id
        self.uri = uri
class User:
    def __init__(self, name, user_id, uri):
        self.name = name
        self.user_id = user_id
        self.uri = uri
