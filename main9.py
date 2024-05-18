import requests
from bs4 import BeautifulSoup

# siteDate = requests.get('https://coinmarketcap.com/').text
# print(siteDate)

# siteParse = siteDate.split('<span>')
# for element in siteParse:
#     print(element)

# print(siteParse[0])
# print()
# print(siteParse[1])

siteDate = requests.get('https://coinmarketcap.com/')
print(siteDate.status_code)

siteParse = BeautifulSoup(siteDate.text, features='html.parser')
# <div class="sc-9d064f2d-0 cAhksY fall"><span>$67,139.85</span></div>
rates = siteParse.find_all(name='div', attrs={'class': 'sc-9d064f2d-0'})

for rate in rates:
    print(rate.find_next('span').text)
