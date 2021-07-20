import requests
from bs4 import BeautifulSoup
import locale
import sys
import time
import random
import codecs

print(locale.getpreferredencoding())
print(sys.stdout.encoding)
print("Парсим закупки по 223 ФЗ по ссылкам")
#sys.stdout = codecs.getwriter('cp866')(sys.stdout,'replace')

# итерация по строкам
# Файл со ссылками
url_file = open('urllist_geneal_info.txt','r')
# Итоговый CSV файл
file_to_write = open('general_data.csv', 'w', encoding='utf-8')
# Без агента работает через раз
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

def getSction(tag, nameSection):
    result=''
    findtag = tag.find(text=nameSection)
    if (findtag!=None):
             dogovorNumber=tag.find_all(['td'])
             result=(probel.join(dogovorNumber[1].text.split()))
             print (nameSection+'='+result)
    return result

  
for url in url_file.readlines():
#   file_to_write.write(url)
   time.sleep(random.randint(1, 3))
# У ссылки отнимаем последний символ, это конец строки, иначе не работает   
   url=url[:-1]
   response = requests.get(url, headers=HEADER)
   print(url)
   responseTxt = response.text
   soup = BeautifulSoup(response.text, 'lxml')
   
   
# Все теги   
#   tags = soup.find_all(['h2', 'p','div','td'])
# Тег td
   tags = soup.find_all(['tr'])
   str=url+';'
   probel=" "
   for tag in tags:
       dogovorNumber = getSction(tag, 'Номер договора')
       if (dogovorNumber!=''): 
                            str=str+dogovorNumber+';'
	   
       predmetdogovora = getSction(tag, 'Предмет договора')	   
       if (predmetdogovora!=''): 
                            str=str+predmetdogovora+';'

       predmetdogovora = getSction(tag, 'Дата заключения договора')	   
       if (predmetdogovora!=''): 
                            str=str+predmetdogovora+';'

       predmetdogovora = getSction(tag, 'Полное наименование заказчика')	   
       if (predmetdogovora!=''): 
                            str=str+predmetdogovora+';'

   # Просто выводим тег для отладки			 
   #print(" ".join(tag.text.split()))
   file_to_write.write(str+'\r'+'\n')
   
url_file.close()
file_to_write.close()