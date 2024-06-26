from billboard import BillBoard
from authenticationspotify import Authentication

date = input("Which year would you like to travel to? Type in format YYYY-MM-DD :")
year = date.split("-")[0]

billboard = BillBoard(date)
song_list = billboard.song_collection()

auth = Authentication()
uri_search = auth.search_uri(song_list, year)
playlist_creation = auth.create_playlist()
