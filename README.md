# Spotify-Data-Downloader

A program made to download in batch all the playlists an account has made.



--- 

## Dependencies

- Spotipy

--- 

## Running Program

You will need to setup a Spotify Application on their developer site.

Then, you will have to set the following environment variables with the information from your spotify app:

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

I suggest using `'http://localhost:8888/callback'` for the `SPOTIPY_REDIRECT_URI`.
