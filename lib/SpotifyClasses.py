#!/usr/bin/env python3

class Playlist:
    tracks = []
    def __init__(self, title, description, owner, pl_id, pl_snapshot_id, uri):
        self.title = title
        self.description = description
        self.owner = owner
        self.pl_id = pl_id
        self.pl_snapshot_id = pl_snapshot_id
        self.uri = uri

class Track:
    def __init__(self, name):
        self.name = name
class TrackEntry:
class Album:
    def __init__(self):
        pass
class User:
    def __init__(self, name, user_id, uri):
        self.name = name
        self.user_id = user_id
        self.uri = uri
