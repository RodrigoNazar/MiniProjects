
from tidalapi import Session, playlist, user
import json

with open('credentials.json', 'r') as credentials_file:
    credentials = json.loads(credentials_file.read())

# Lolo ID
user_id = '183890341'

# Momentos Robados ID
playlist_id = 'b1a8eb10-48c3-434a-9a20-5963d5fe81c3'

session = Session()

session.load_oauth_session(
    credentials['token_type'], 
    credentials['access_token'], 
    credentials['refresh_token'], 
    credentials['expiry_time']
)

print('Playlist Momentos robados', playlist.UserPlaylist(session, playlist_id).tracks())
print()
print('Playlists de Lolo', user.LoggedInUser(session, user_id).playlists())
