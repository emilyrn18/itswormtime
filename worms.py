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

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get read access to your library
scope = 'user-library-read user-read-private user-read-playback-state user-modify-playback-state'

#token = 'BQDWkJXMVemN_F9uzDtLLwOeLqWgM3-sR8qphkfS3Zw09aPVA7ZIFn0uNkU_hOjQ2Xn-8nXJwwsj-6Ch1ytJExgInfpc2i5fnRu6oLaQll2gAdDUqeCaj9VMLjqKTfa6mXpYzCLggzAGD8P2cps'

try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

if token:
    spotifyObject = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
