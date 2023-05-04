import requests


def get_naver_shopping(item):
    URL = f'https://openapi.naver.com/v1/search/shop.json?query={item}'

    headers = {
        'X-Naver-Client-Id': 'NhTugMmU0157d_E7bekC',
        'X-Naver-Client-Secret': 'nlkJPixmWg'
    }

    res = requests.get(URL, headers=headers).json()
    result = res['items'][0]
    msg = f"{result['title']}) {result['lprice']}원 \n {result['link']}"
    return msg


# print(get_naver_shopping('오렌지'))
