import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?query=%EB%A1%9C%EB%98%90'
# URL 로 요청을 보내고, 응답을 받는다.
res = requests.get(URL)
# 응답으로 받은 HTML 문서를 구문 분석한다.
soup = BeautifulSoup(res.text, 'html.parser')
# 구문 분석된 결과에서, 원하는 데이터를 선택한다.

no1 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type1').text
no2 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span:nth-child(2)').text
no3 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span:nth-child(3)').text
no4 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type3').text
no5 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type4').text
no6 = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number > span.ball.type5').text
bonus_no = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > div > div.bonus_number > span').text

prize = soup.select_one('#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_area > div > div > div:nth-child(2) > div.win_number_box > p > strong').text

print('당첨번호', no1, no2, no3, no4, no5, no6)
print('보너스번호', bonus_no)
print(prize)
