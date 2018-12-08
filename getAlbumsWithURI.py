import spotipy
import json
#from credentials import client_credentials_manager

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("Give the artist's URI: ")
artist_URI = input()
print()

artist = sp.artist(artist_URI)
artist_name = artist['name']
results = sp.artist_albums(artist_URI)
albums = []
albums.extend(results['items'])

while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

albums.sort(key = lambda album:album['name'].lower()) 

for album in albums:
    if album['artists'][0]['name'] == artist_name:
        print(album['name'] + ':\n')
        results = sp.album_tracks(album['id'])
        tracks = []
        tracks.extend(results['items'])
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        
        for index, track in enumerate(tracks):
            artists = []
            artists.extend(track['artists'])
            
            
            if len(artists) == 1:
                print('\t' + str(index+1) + '. ' + track['name'])
                continue
            print('\t' + str(index+1) + '. ' + track['name'] + ' (ft. ', end="")

            for index in range(len(artists)):
                if index == 0:
                    continue
                if index == (len(artists) - 1):
                    print(artists[index]['name'] + ')')
                    break
                print(artists[index]['name'] + ', ', end = "")
        print()