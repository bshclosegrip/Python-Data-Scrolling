from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests

page = urlopen("https://world.taobao.com/")
document = page.read()
page.close()

soup = bs(document, 'html5lib')

while True:
    print("검색할 중국어를 입력해주세요 : ")
    word = input()

    s = requests.Session()
    dict_page = "https://world.taobao.com/" + word
    # dict_page = "https://world.taobao.com/" + word
    html = ""
    resp = s.get(dict_page)
    if resp.status_code == 200:
        html = resp.text
    soup = bs(html, 'html.parser')

    result = ''

    # 중국어
    try:
        result += '중국어 : ' + soup.find('div', {'class': 'cn_dic_section search_result dic_cn_entry'}) \
            .find('dl', {'class': 'dic_search_result'}).find('dd')\
            .find('em').next_sibling\
            .strip() + '\n'
    except:
        result += '중국어 단어를 찾지 못했습니다.\n'

    print(result)
    print('다시 검색하시겠습니까? (Y / N)')
    re = input()
    if not (re == 'Y' or re == 'y'):
        break
    print(result)


questions = soup.find(id="questions")
questions_list = questions.find_all(word, class_="question-hyperlink")

for question in questions_list:
    print(question.get_text())
    print('http://stackoverflow.com' + question.get('href'))