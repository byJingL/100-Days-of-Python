import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
pp = pprint.PrettyPrinter(indent=4)

ID = os.environ.get('Client_ID')
SECRET = os.environ.get("Client_Secret")
URI = os.environ.get("redirect_uri")

# Todo 1. Get data from user
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

# Todo 2. Get Top-100-Songs from Billboard on specific day
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
web_page = response.text

# with open("web.txt", "w") as file:
#     file.write(response.text)
# with open("web.txt") as file:
#     web_page = file.read()

soup = BeautifulSoup(web_page, "html.parser")
songs = soup.select("li ul li h3")
songs_titles = [song.getText().replace("\n", "").replace("\t", "") for song in songs]
print(songs_titles)

# Todo 3. Create playlist in Spotify using "spotify module and Spotify API"
# Autenticate with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=ID,
                              client_secret=SECRET,
                              redirect_uri=URI,
                              scope="playlist-modify-private",
                              cache_path="token.txt",
                              show_dialog=True,))
user_id = sp.current_user()["id"]
year = travel_date.split("-")[0]

# create song URIs
song_URIs = []
for title in songs_titles:
    result = sp.search(q=f"track: {title} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

# create the playlist
playlist_name = f"{travel_date} Billboard 100"
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name,
                                       public=False, description='')
pp.pprint(new_playlist)
# From above print can get playlist id and link
playlist_id = new_playlist["id"]
playlist_link = new_playlist["external_urls"]["spotify"]

# add all the songs
sp.playlist_add_items(playlist_id, song_URIs, position=None)

# print the link of the playlist for sharing
print(playlist_link)
