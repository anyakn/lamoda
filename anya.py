from bs4 import BeautifulSoup
import requests


url = 'https://www.lamoda.ru/catalogsearch/result/?q=%D1%88%D1%82%D0%B0%D0%BD%D1%8B+%D0%BA%D0%B0%D1%80%D0%B3%D0%BE&submit=y&gender_section=women&sort=price_asc'


r = requests.get(url)
text = r.text
print(text)

#soup = BeautifulSoup(r.text, "html.parser")
#number = soup.find('div', class_='x-product-card-description')
#print(number)
#print(soup)
