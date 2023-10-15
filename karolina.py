import requests

query = input('Введите ваш запрос: ')
query = query.replace(' ', '+')
query = query.lower()
url = 'https://www.lamoda.ru/catalogsearch/result/?q='+query+'&sort=price_asc'

# url = url+'&page='+ str(number)
r = requests.get(url)

text = r.text
i = text.find('<a href=')
new_text = text[i:]
print(new_text)

'''
with open('output.txt', 'w+', encoding='utf8') as f_out:
    print(r.text, file=f_out)

'''

