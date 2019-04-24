from bs4 import BeautifulSoup as bs
import requests

headers={'accept':'*/*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

base_url='https://hh.ru/search/vacancy?search_period=3&area=1&text=Python&page=0'


def hh_parce(base_url,headers):
    session=requests.Session()
    request=session.get(base_url,headers=headers)
    if request.status_code==200:
        soup=bs(request.content,'html.parser')
        divs=soup.find_all('div',attrs={'data-qa':"vacancy-serp__vacancy"})
        for div in divs:
            title=div.find('a',attrs={'data-qa':"vacancy-serp__vacancy-title"}).text
            href=div.find('a',attrs={'data-qa':"vacancy-serp__vacancy-title"})['href']
            requement=div.find('div',attrs={'data-qa':"vacancy-serp__vacancy_snippet_requirement"}).text
            print(title)
            print(href)
            print(requement)
        
    else:
        print('ERROR')

hh_parce(base_url,headers)
