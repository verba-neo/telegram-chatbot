import requests

URL = 'https://openapi.naver.com/v1/search/shop.json?query=초단초점빔프로젝터'

headers = {
    'X-Naver-Client-Id': 'NhTugMmU0157d_E7bekC',
    'X-Naver-Client-Secret': 'nlkJPixmWg'
}

res = requests.get(URL, headers=headers)

print(res.text)