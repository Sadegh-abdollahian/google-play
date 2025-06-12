import requests


def send_otp(code, phone_number):
    api_key = "your_api_key"
    sender = "your_sender"
    url = f"https://api.sms-webservice.com/api/V3/Send?ApiKey={api_key}&Text={code}&Sender={sender}&Recipients={phone_number}"

    payload = {}
    headers = {}
    print("*\n" * 5, code, "*\n" * 5)
    # try:
    #     response = requests.get(url, headers=headers, data=payload)
    #     response.raise_for_status()
    #     print(response.text)
    # except requests.exceptions.HTTPError as err:
    #     print(err)
