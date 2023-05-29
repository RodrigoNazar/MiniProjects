import tidalapi
import json

session = tidalapi.Session()

login, future = session.login_oauth()

print("Open the URL to log in", login.verification_uri_complete)

future.result()
print(session.check_login())

token_type = session.token_type
access_token = session.access_token
refresh_token = session.refresh_token # Not needed if you don't care about refreshing
expiry_time = session.expiry_time

print(
    'Credenciales obtenidas!\n\n'
    f'token_type = {token_type}\n',
    f'access_token = {access_token}\n',
    f'refresh_token = {refresh_token}\n',
    f'expiry_time = {expiry_time}\n',
)

credentials = {
    'token_type': token_type,
    'access_token': access_token,
    'refresh_token': refresh_token, # Not needed if you don't care about refreshing
    'expiry_time': expiry_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
}
'2023-06-05 18:59:45.938033'

print('credentials', credentials)

with open('credentials.json', 'w') as credentials_file:
    credentials_file.write(json.dumps(credentials, indent=2))

print('\n\nTus nuevas credenciales de Acceso estan listas!')
