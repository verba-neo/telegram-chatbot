import requests
from bs4 import BeautifulSoup

# URL 과 토큰 세팅
TOKEN = '6289166604:AAHMii9LEVCMx4vyw7ezqmehfQ5NAy0uxGk'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

# getUpdate 로 메시지 받아오기 
response = requests.get(BASE_URL + '/getUpdates').json()
# 마지막 메시지의 발신자/내용 가져오기
last_chat_id = response['result'][-1]['message']['chat']['id']
last_msg = response['result'][-1]['message']['text']

if last_msg == '주식':
    URL = 'https://finance.naver.com/sise/'
    # URL 로 요청을 보내고, 응답을 받는다.
    res = requests.get(URL)
    # 응답으로 받은 HTML 문서를 구문 분석한다.
    soup = BeautifulSoup(res.text, 'html.parser')
    # 구문 분석된 결과에서, 원하는 데이터를 선택한다.
    kospi = soup.select_one('#KOSPI_now').text
    kosdaq = soup.select_one('#KOSDAQ_now').text
    kospi200 = soup.select_one('#KPI200_now').text
    return_msg = f'KOSPI: {kospi}, KOSDAQ: {kosdaq}, KOSPI200: {kospi200}'

elif last_msg in ['로또', 'lotto', 'Lotto']:
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1065'
    res = requests.get(URL)
    data = res.json()
    numbers = []
    for i in range(1, 7):
        numbers.append(data[f'drwtNo{i}'])
    return_msg = f"번호: {numbers}, 보너스: {data['bnusNo']}, 상금: {data['firstWinamnt']}"

elif last_msg.split()[0] == '쇼핑':
    URL = f'https://openapi.naver.com/v1/search/shop.json?query={last_msg.split()[1]}'
    headers = {
        'X-Naver-Client-Id': 'NhTugMmU0157d_E7bekC',
        'X-Naver-Client-Secret': 'nlkJPixmWg'
    }
    res = requests.get(URL, headers=headers).json()
    return_msg = res['items'][0]

else:
    return_msg = '모르는 명령어 입니다 😢'

# 마지막 메시지의 발신자에게 답장할 메시지를 보냄
requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={return_msg}')
