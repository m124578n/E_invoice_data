import requests
import json


def get_invoice_jwt(token, invoiceNumber, randomNumber, invoiceDate, captcha):
    headers = {
        'authority': 'service-mc.einvoice.nat.gov.tw',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
        'content-type': 'application/json',
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

    '2024-03-29T09:34:52.560Z'

    json_data = {
        'invoiceNumber': invoiceNumber,
        'invoiceDate': invoiceDate,
        'personalCode': '',
        'randomNumber': randomNumber,
        'captcha': captcha,
        'token': token,
    }

    response = requests.post(
        'https://service-mc.einvoice.nat.gov.tw/btc/cloud/api/btc601w/getInvoiceJwt',
        headers=headers,
        json=json_data,
    )
    try:
        json.loads(response.text)
        return False, response.text
    except Exception as e:
        return True, response.text
