# Imports
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Connects to  Client ID, SECRET, and username
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
