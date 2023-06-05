'''import urllib.request

opener = urllib.request.build_opener() #создаем объект ОБРОБНИКА
response = opener.open('https://httpbin.org/get') # реализуем подключение к целевой странице
print(response.read()) # выводим полученный ЗМИСТ


import requests
response = requests.get('https://httpbin.org/get')
print(response.content)'''

'''import requests
response = requests.get('https://httpbin.org/get')
print(response.content)
print(f'Datatype - {type(response.content)}')

print(response.text)
print(f'Datatype - {type(response.text)}')'''


'''import requests
response = requests.post('https://httpbin.org/post', data='Test info', headers={'h1':'Test title'})
print(response.text)'''

'''import requests
response = requests.post('https://httpbin.org/post', data={'Test form':'My form'}, headers={'h1':'Test title'})
print(response.text)'''

'''import requests

res_parse_list = []
response = requests.get('https://coinmarketcap.com/')
#print(response.text)
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith('$'):
        #print(parse_elem_1)
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if parse_elem_2.startswith('$') and parse_elem_2[1].isdigit():
                #print(parse_elem_2)
                res_parse_list.append(parse_elem_2)
while True:
    choice = input('Enter btc, eth, the for USD rates or exit: ')
    if choice == 'btc':
        bitcoin_exchange_rate = res_parse_list[0]
        print(bitcoin_exchange_rate)
    elif choice == 'eth':
        bitcoin_exchange_rate1 = res_parse_list[1]
        print(bitcoin_exchange_rate1)
    elif choice == 'the':
        bitcoin_exchange_rate2 = res_parse_list[2]
        print(bitcoin_exchange_rate2)
    elif choice == 'exit':
        print('Good luck!')
        break
    else:
        print('Wrong action!')'''


'''from bs4 import BeautifulSoup
import requests

response = requests.get('https://coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('a', {'href':'/currencies/bitcoin/markets/'})
    #for elem in soup_list:
        #print(elem)
    res = soup_list[0].find('span')
    print(res.text)'''

