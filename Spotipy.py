# import os
# import sys
# import json
# import spotipy
# import webbrowser
# # This won't import correctly for some reason
# import spotipy.util as util
# from json.decoder import JSONDecodeError

# # Gets username from terminal
# username = sys.argv[1]

# # user ID = 12139911168


# try:
#     token = util.promp_for_user_token(username)
# except:
#     os.remove(f".cache-{username}")
#     token = util.promp_for_user_token(username)

# spotifyObject = spotipy.Spotify(auth=token)

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

cid = '<INSERT CLIENT ID>'
secret = '<INSERT CLIENT SECRET>'
username = ""

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get read access to your library
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
