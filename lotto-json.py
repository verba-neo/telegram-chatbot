import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1065'
res = requests.get(URL)

data = res.json()

for i in range(1, 7):
    print(data[f'drwtNo{i}'])
    
print(data['bnusNo'])
print(data['firstWinamnt'])