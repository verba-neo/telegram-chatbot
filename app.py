from flask import Flask, request
import requests
import utils

app = Flask('telegram-chatbot')

TOKEN = '6289166604:AAHMii9LEVCMx4vyw7ezqmehfQ5NAy0uxGk'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'


@app.route('/telegram', methods=['POST'])
def telegeram():
    data = request.json
    print('TELEGRAM에서 요청이 들어왔다!')
    chat_id = data['message']['from']['id']
    message = data['message']['text']

    if message == '주식':
        return_msg = utils.get_kospi()
    elif message in ['로또', 'lotto', 'Lotto']:
        return_msg = utils.get_lotto()
    elif message.split()[0] == '쇼핑':
        item = message.split()[1]
        return_msg = utils.get_naver_shopping(item)
    else:
        return_msg = '모르는 명령어 입니다 😢'
    
    requests.get(BASE_URL + f'/sendMessage?chat_id={chat_id}&text={return_msg}')
    # Response
    return 'Telegram CHATBOT'



# '/hello' 이렇게 요청이 들어오면
@app.route('/hello')
def hello():
    # 'Hellow World!!!' 라고 응답 해라.
    return 'Hello World!!!'


if __name__ == '__main__':
    app.run(port=80, debug=True)

