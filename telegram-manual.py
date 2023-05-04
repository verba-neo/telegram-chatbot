import requests
from bs4 import BeautifulSoup
import utils

# URL 과 토큰 세팅
TOKEN = '6289166604:AAHMii9LEVCMx4vyw7ezqmehfQ5NAy0uxGk'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

# getUpdate 로 메시지 받아오기 
response = requests.get(BASE_URL + '/getUpdates').json()
# 마지막 메시지의 발신자/내용 가져오기
last_chat_id = response['result'][-1]['message']['chat']['id']
last_msg = response['result'][-1]['message']['text']

if last_msg == '주식':
    return_msg = utils.get_kospi()

elif last_msg in ['로또', 'lotto', 'Lotto']:
    return_msg = utils.get_lotto()

elif last_msg.split()[0] == '쇼핑':
    item = last_msg.split()[1]
    return_msg = utils.get_naver_shopping(item)
    
else:
    return_msg = '모르는 명령어 입니다 😢'

# 마지막 메시지의 발신자에게 답장할 메시지를 보냄
requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={return_msg}')
