import requests

url = 'https://www.google.com'

def internet():
    while True:
        try:
            requests.get(url, timeout=5)
            return True
        except:
            return False