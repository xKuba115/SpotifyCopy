import requests
import json
from bs4 import BeautifulSoup

def GetImageSrc(name):
    url = f'https://en.wikipedia.org/wiki/{name}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()
    try:
        image = soup.find( class_="infobox-image")
        src = image.img['src'][2:]
        return src

    except Exception as e:
        print(f"Error: {e}")
        return None


 












