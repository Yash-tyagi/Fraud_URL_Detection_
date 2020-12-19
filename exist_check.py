import re
def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

x = 'xini.eu/00Qe'
url = formaturl(x)
print(url)
import requests
try:
    request = requests.head(url)
    if request.status_code == 200:
        print('Web site exists')
except:
    print('Web site does not exist') 
    
