from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import json

SPOTIPY_CLIENT_ID = YOUR_CLIENT_ID
SPOTIPY_CLIENT_SECRET = YOUR_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"


# Bill Board List of 100 songs for any date user specifies.

date_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_to_travel}"
year = date_to_travel.split('-')[0]
print(year)
response = requests.get(URL)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
all_titles = []
title_tag = soup.find_all(name="li", class_="lrv-u-width-100p")
for tag in title_tag:
    music_title = tag.find(name="h3", id="title-of-a-story")
    if music_title is not None:
        all_titles.append(music_title.getText().strip())
print(all_titles)
print(len(all_titles))


# using Spotipy library to access spotify API in order to create a playlist of 100 songs from Bill Board.

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path="token.txt"

    )
)

user_id = sp.current_user()["id"]
song_uri_list = []
for song in all_titles:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. SKIPPED.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date_to_travel} Billboard Top 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)
