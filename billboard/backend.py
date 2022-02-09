import spotify
from spotipy.oauth2 import SpotifyOAuth
sp = spotify.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        
)
)