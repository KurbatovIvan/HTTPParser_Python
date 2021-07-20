import requests
from bs4 import BeautifulSoup

#url = 'https://zakupki.gov.ru/223/contract/public/contract/view/general-information.html?style44=false&id=11742676'
url ='https://zakupki.gov.ru/epz/contractfz223/search/results.html?searchString=кислород&morphology=on&search-filter=Дате+размещения&savedSearchSettingsIdHidden=&statuses_0=on&statuses=0&priceFrom=&priceTo=&currencyId=-1&contract223DateFrom=&contract223DateTo=&publishDateFrom=&publishDateTo=&customerPlace=5277389&customerPlaceCodes=38000000000&sortBy=BY_UPDATE_DATE&pageNumber=4&sortDirection=false&recordsPerPage=_50&showLotsInfoHidden=false'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('td')
	

# Извлечь все ссылки
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])