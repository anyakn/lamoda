import urllib

query = input('Введите ваш запрос: ')
query = query.replace(' ', '+')
query = query.lower()
url = f"https://google.com/search?q={query}"

print(url)
#response = requests.get(url)
# with open('output.txt', 'w+', encoding='utf8') as f_out:
#    print(response.text, file=f_out)