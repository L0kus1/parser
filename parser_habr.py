import requests
from bs4 import BeautifulSoup
import sys

# Habr

#main page
text = input()
url = 'https://habr.com/ru/articles/page1/'
print(url + ':')
response = requests.get(url).text
links = {}
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('h2', class_ = 'tm-title tm-title_h2'):
    title = article.a.span.text
    
    if text in title.lower():
        link = 'https://habr.com'+article.a['href']
        print(title, link)
        links[link] = title

#2
url = 'https://habr.com/ru/articles/page2/'
print(url + ':')
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('h2', class_ = 'tm-title tm-title_h2'):
    title = article.a.span.text
    
    if text in title.lower():
        link = 'https://habr.com'+article.a['href']
        print(title, link)
        links[link] = title


#3
url = 'https://habr.com/ru/articles/page3/'
print(url + ':')
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('h2', class_ = 'tm-title tm-title_h2'):
    title = article.a.span.text
    
    if text in title.lower():
        link = 'https://habr.com'+article.a['href']
        print(title, link)
        links[link] = title

#4
url = 'https://habr.com/ru/articles/page4/'
print(url + ':')
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('h2', class_ = 'tm-title tm-title_h2'):
    title = article.a.span.text
    
    if text in title.lower():
        link = 'https://habr.com'+article.a['href']
        print(title, link)
        links[link] = title


#5
url = 'https://habr.com/ru/articles/page5/'
print(url + ':')
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('h2', class_ = 'tm-title tm-title_h2'):
    title = article.a.span.text
    
    if text in title.lower():
        link = 'https://habr.com'+article.a['href']
        print(title, link)
        links[link] = title


print(links)

number = 1

try:
    for url1 in links:
        print(url1,'-->', links[url1])
        name = str(links[url1]).replace('"', '').replace('*', '').replace('.', '') + '.txt'
        output_file = open(name, 'w',  encoding='utf-8')
        print(url1)
        response = requests.get(url1)
        response.raise_for_status()
        data1 = BeautifulSoup(response.text, 'html.parser')
        
        for article in data1.find_all('p'):
            output_file.write(article.text)

        output_file.close()
        number += 1
except Exception as e:
    print(f"Error: {e}")





#mail

# url = 'https://news.mail.ru/'
# response = requests.get(url).text

# data = BeautifulSoup(response, 'html.parser')
# text = input()
# for article in data.find_all('span', class_ = 'newsitem__title link-holder'):
#     title = article.a.span.text
#     #link = 'https://habr.com'+article.a['href']
#     print(title)