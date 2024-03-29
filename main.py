from captcha import get_captcha
from get_invoice_jwt import get_invoice_jwt
from get_invoice_data import get_invoice_data
from datetime import datetime


if __name__ == '__main__':
    print("start")
    token, image = get_captcha()
    captcha = input("請輸入captcha：")
    invoiceNumber = input("請輸入發票：")
    randomNumber = input("請輸入隨機碼：")
    invoiceDate = input("請輸入日期 e.g. 2024-01-01：")
    invoiceDate += datetime.utcnow().strftime("T%H:%M:%S") + '.000Z'
    OK, result = get_invoice_jwt(token, invoiceNumber, randomNumber, invoiceDate, captcha)
    if OK:
        response = get_invoice_data(result)
        print(response)
    else:
        print(result)


