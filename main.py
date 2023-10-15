import requests

query = input('Введите ваш запрос: ')

query = query.replace(' ', '+')
query = query.lower()
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'
