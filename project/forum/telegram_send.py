import requests
from .token import token


def send_telegram(text_for_tg):
	chat_id = '-1001889058020'
	url = f'https://api.telegram.org/bot{token}/sendMessage'
	data = {'chat_id': chat_id, 'text':text_for_tg}
	response = requests.post(url, json=data)