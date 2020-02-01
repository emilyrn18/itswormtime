# Import libraries
import os
import sys
import json
import webbrowser
from json.decoder import JSONDecodeError
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Access token: BQDWkJXMVemN_F9uzDtLLwOeLqWgM3-sR8qphkfS3Zw09aPVA7ZIFn0uNkU_hOjQ2Xn-8nXJwwsj-6Ch1ytJExgInfpc2i5fnRu6oLaQll2gAdDUqeCaj9VMLjqKTfa6mXpYzCLggzAGD8P2cps

# Connects to  Client ID, SECRET, and username
cid = '5239ca0b44d74a8188734bae8ad6e330'
secret = '6df461582d434e01bdfb7bba529d9b16'
#username = "12139911168"
username = sys.argv[1]

# applies your client ID and secret
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get read access to your library
scope = 'user-library-read user-read-private user-read-playback-state user-modify-playback-state'

#token = 'BQDWkJXMVemN_F9uzDtLLwOeLqWgM3-sR8qphkfS3Zw09aPVA7ZIFn0uNkU_hOjQ2Xn-8nXJwwsj-6Ch1ytJExgInfpc2i5fnRu6oLaQll2gAdDUqeCaj9VMLjqKTfa6mXpYzCLggzAGD8P2cps'

# Obtains token based on your username and scope
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

# creates a spotifyObject
if token:
    spotifyObject = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# grabs available spotify devices
devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

# Get track information
track = spotifyObject.current_user_playing_track()
print(json.dumps(track, sort_keys=True, indent=4))
print()
print(track)
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != "":
    print("Currently playing " + artist + " - " + track)

# Analyze current track


# Spotify interactivity
choice = 0

while choice not 1:

    print()
    print(">>> Welcome to Spotify " + username + " :)")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Enter your choice: ")

    # Search for artist
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?:")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery, 1, 0, "artist")

        # Print artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album details
        trackURIs = []
        trackArt = []
        z = 0
