import requests

query = input('Введите ваш запрос: ')
query = query.replace(' ', '+')
query = query.lower()
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'

print(url)
r = requests.get(url)
with open('output.txt', 'w+', encoding='utf8') as f_out:
    print(r.text, file=f_out)

