
import requests

url = 'http://shorturl.at/uzIR8'
resp = requests.head(url, allow_redirects=True) # so connections are recycled

print(resp.url)