import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

import requests
from bs4 import BeautifulSoup
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2021-05-15"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

bb_page = response.text

soup = BeautifulSoup(bb_page, "html.parser")
# print(soup.prettify())
title_ids = soup.select(selector='li h3')
# print(title_ids)

song_names = [title_id.get_text().replace("\n", "")
          for title_id in title_ids][:100]
# print(titles)
# print(len(titles))

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="billboard/token.txt"       
        )
)
user_id = sp.current_user()["id"]
print(user_id)


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
