#!/usr/bin/env python3

class Playlist(dict):
    def __init__(self, title, description, owner, pl_id, pl_snapshot_id, uri):
        dict.__init__(self, title=title, description=description, owner=owner, pl_id=pl_id, pl_snapshot_id=pl_snapshot_id, uri=uri)
        self['track_entries'] = []
        # self.title = title
        # self.description = description
        # self.owner = owner
        # self.pl_id = pl_id
        # self.pl_snapshot_id = pl_snapshot_id
        # self.uri = uri

class TrackEntry(dict):
    def __init__(self, added_at, added_by, track):
        dict.__init__(self, added_at=added_at, added_by=added_by, track=track)
        # self.added_at = added_at
        # self.added_by = added_by
        # self.track = track
class Track(dict):
    def __init__(self, name, album, artists, disc_number, track_number, track_id, uri):
        dict.__init__(self, name=name, album=album, artists=artists, disc_number=disc_number, track_number=track_number, track_id=track_id, uri=uri)
        # self.name = name
        # self.album = album
        # self.artists = artists
        # self.disc_number = disc_number
        # self.track_number = track_number
        # self.track_id = track_id
        # self.uri = uri
class Episode(dict):
    def __init__(self, name, description, show, episode_id, uri):
        dict.__init__(self, name=name, description=description, show=show, episode_id=episode_id, uri=uri)
        # self.name = name
        # self.description = description
        # self.show = show
        # self.episode_id = episode_id
        # self.uri = uri
class Show(dict):
    def __init__(self, name, description, publisher, show_id, uri):
        dict.__init__(self, name=name, description=description, publisher=publisher, show_id=show_id, uri=uri)
        # self.name = name
        # self.description = description
        # self.publisher = publisher
        # self.show_id = show_id
        # self.uri = uri
class Album(dict):
    def __init__(self, name, album_id, artists, uri):
        dict.__init__(self, name=name, album_id=album_id, artists=artists, uri=uri)
        # self.name = name
        # self.album_id = album_id
        # self.artists = artists
        # self.uri = uri
class Artist(dict):
    def __init__(self, name, artist_id, uri):
        dict.__init__(self, name=name, artist_id=artist_id, uri=uri)
        # self.name = name
        # self.artist_id = artist_id
        # self.uri = uri
class User(dict):
    def __init__(self, name, user_id, uri):
        dict.__init__(self, name=name, user_id=user_id, uri=uri)
        # self.name = name
        # self.user_id = user_id
        # self.uri = uri
