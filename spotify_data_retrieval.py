import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import numpy as np
import pprint as pp

cid = '0a53db057e4541fd809634e425b3aca7'
secret = 'fd8177608e094a36ac588f3603c39f43'

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



track_id = []


year_range = 1
# num has to be divisible by the limit
number_of_songs = 100
query_limit = 50

# Song title, Song Artist, Song Id, acousticness, dancability
song_array = np.empty((number_of_songs, 4), dtype=float)



# track_results = sp.search(q='year:2021', type='track:items', limit=50, offset=1)
# track_arr = track_results['tracks']['items']

for year in range(year_range):
    search_year = 'year:20' + str(21 - year)
    print(search_year)
    for i in range(0, number_of_songs, query_limit):
        track_results = sp.search(q=search_year, type='track', limit=query_limit, offset=i)
        tracks = track_results['tracks']['items']
        for j in range(len(tracks)):
            track_id.append(tracks[j]['id'])
        
        song_features = sp.audio_features(track_id[i:i+query_limit-1])
            #might be better to call outside with 50 is due to internet speed
            
        for j in range(len(song_features)):
            song_array[i+j,0] = song_features[j]['acousticness']
            song_array[i+j,1] = song_features[j]['energy']
            song_array[i+j,2] = song_features[j]['instrumentalness']
            song_array[i+j,3] = song_features[j]['valence']

        

for i in range(10):
    print(track_id[i], song_array[i]) 

