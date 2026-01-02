import base64

consumer_key = 'fHs5RHHsKxtgSEvCS1F2YW3L0xnJJ9VDvkAbs7DEtoHqQcEX'
consumer_secret = '4pFvx1cACzPWs3ynALKVKdG7zXNVqbpYDqwnLWwPiJJrFkAX7XGYhn4Pf55XfYVp``'

combined = f'{consumer_key}:{consumer_secret}'
encoded = base64.b64encode(combined.encode())

basic_auth = f'Basic {encoded.decode()}'
print(combined)