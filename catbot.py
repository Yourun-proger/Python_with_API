from PIL import Image
from requests import get
from urllib.request import urlopen

def get_url():
    req = get("https://api.thecatapi.com/v1/images/search")
    img_url = req.json()[0]['url']
    return img_url
url = get_url()
img = Image.open(get(url, stream=True).raw)
img.show()
