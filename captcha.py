import base64
import json
import requests
from PIL import Image
from io import BytesIO


def get_captcha():
    headers = {
        'authority': 'service-mc.einvoice.nat.gov.tw',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
        'origin': 'https://www.einvoice.nat.gov.tw',
        'referer': 'https://www.einvoice.nat.gov.tw/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    response = requests.get('https://service-mc.einvoice.nat.gov.tw/act/login/api/act002i/captcha', headers=headers)

    res = json.loads(response.text)
    image_data = base64.b64decode(res['image'])
    image = Image.open(BytesIO(image_data))
    image.show()
    return res['token'], res['image']


