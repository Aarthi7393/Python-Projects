import spotipy
from spotipy.oauth2 import (SpotifyOAuth)
import pprint
import os

# proxy = "http://internet.ford.com:83"
# os.environ ['http_proxy'] = proxy
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy


REDIRECT_URI = "http://example.com"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")



class Authentication:
    def __init__(self):
        print(CLIENT_ID)
        self.uri_list = []
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope="playlist-modify-private",
                show_dialog=True
            ))
        self.user_id = self.sp.current_user()["id"]

    def search_uri(self, song_list, year):
        album_list = song_list

        for name in album_list:
            uri = self.sp.search(q=f"track: {name} year: {year}", limit=1)
            try:
                self.uri_list.append(uri["tracks"]["items"][0]["uri"])
            except:
                pass

    def create_playlist(self):
        playlist_name = "My Time Machine Playlist"
        #Create Playlist
        playlist = self.sp.user_playlist_create(user = self.user_id, name=playlist_name, public=False)
        print(playlist)
        playlist_id = playlist["id"]
        #Add items to playlist
        self.sp.playlist_add_items(playlist_id, self.uri_list)
        print(playlist_id)
