import re
from datetime import datetime
from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()

url = 'https://announcements.bybit.com/en-US/?category=&page=1'
url_new_list = 'https://announcements.bybit.com/en-US/?category=new_crypto&page=1'

r = session.get(url_new_list)

article_list = r.html.find('.article-list')[0]
last_info = article_list.text.split("\n")[:2]
post_name = re.sub(r"[^\w\s,]", '', last_info[0])

soup = BeautifulSoup(article_list.html, 'html.parser')
first_a_tag = soup.find('a', href=True)
link = 'https://announcements.bybit' + first_a_tag['href']

date_object = datetime.strptime(last_info[1], '%b %d, %Y')
formatted_date = date_object.strftime('%d.%m.%y')

print(formatted_date)
print(post_name)
print(link)
ii = 'https://announcements.bybit.com/en-US/article/-new-polyxusdt-powrusdt-perpetual-contracts-bltc5a9ffce74ad45d3/?category=new_crypto'
# article_list = r.html.find('.article-list')
# button = r.html.find('li.ant-menu-item[data-cy="newCrypto"]', first=True)
# script = r.html.find('#__NEXT_DATA__')[0]
# v = button.html.render(script=script.text, reload=False)
# print(button)