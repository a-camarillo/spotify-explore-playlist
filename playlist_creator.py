import json 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open('track_ids.json','r') as f:
    ids = json.load(f)

id_list = ids.values()

scope = "playlist-modify-public"

OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='http://localhost:8888',
                     cache_path='../cache.txt')
token = OAuth.get_cached_token()

sp = spotipy.Spotify(auth_manager=OAuth)

user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(user=user_id,name='Regression Playlist',description='I might like it, I might not')

sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist['id'],tracks=id_list)

