import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "user-top-read"

OAuth = SpotifyOAuth(scope=scope,
                     redirect_uri='http://localhost:8888',
                     cache_path='../cache.txt')
token = OAuth.get_cached_token()

sp = spotipy.Spotify(auth_manager=OAuth)

def get_top_tracks():
    '''Get top user current top tracks'''
    
    top_tracks = sp.current_user_top_tracks(limit=50,time_range='medium_term')
    
    top_track_dict = {}
    for track in top_tracks['items']:
        top_track_dict.update({track['name']:track['id']})
    
    return top_track_dict 

def top_audio_features(top_tracks):
    '''Get audio features from dict of top user tracks'''
    audio_features = {}
    
    for key in top_tracks.keys():
        audio_features.update({key:{}})
    
    features = sp.audio_features(top_tracks.values())

    for key,value in zip(audio_features,features):
        audio_features.update({key:value})
    
    return audio_features

recent_tracklist = get_top_tracks()
top_features = top_audio_features(recent_tracklist)
with open('features.json','w') as file:
   json.dump(top_features, file)






 


