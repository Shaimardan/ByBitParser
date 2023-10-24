from requests_html import HTMLSession

session = HTMLSession()

url = 'https://announcements.bybit.com/en-US/?category=&page=1'

r = session.get(url)

article_list = r.html.find('.article-list')
button = r.html.find('li.ant-menu-item[data-cy="newCrypto"]', first=True)
button.click()
article_list = r.html.find('.article-list')
print(r.html.links)

button = r.html.find('#my-button', first=True)
# button.click()
# r.html.render()
# r.html.finde('.ant-menu-item ant-menu-item-selected ant-menu-item-only-child')


# import requests
# import time
# import random
#
# from bs4 import BeautifulSoup
#
# #   Имитация пользовательского поведения
# url = 'https://announcements.bybit.com/en-US/?category=&page=1'
# user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36']
#
# headers = {
#     'User-Agent': random.choice(user_agents)
# }
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# data = response.text
#
# # Используйте полученные данные
# print(data)