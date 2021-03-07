from PIL import Image
from requests import get


def get_url():
    req = get("https://dog.ceo/api/breeds/image/random")
    img_url = req.json()['message']
    return img_url


url = get_url()
img = Image.open(get(url, stream=True).raw)
img.show()
