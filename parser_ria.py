import requests
from bs4 import BeautifulSoup


# rbk

#main page
text = input()
url = 'https://ria.ru/world/'
print(url + ':')
response = requests.get(url).text
links = {}
data = BeautifulSoup(response, 'html.parser')
for article in data.find_all('a', class_ = "list-item__title"):
    title = article.get_text(strip=True)
    
    if text in title.lower():
        link = article['href']
        print(title, link)
        links[link] = title


print(links)

number = 1

try:
    for url1 in links:
        print(url1,'-->', links[url1])
        name = str(links[url1]).replace('"', '').replace('*', '').replace('.', '') + '.txt'
        output_file = open(name, 'w',  encoding='utf-8')
        response = requests.get(url1)
        response.raise_for_status()
        data1 = BeautifulSoup(response.text, 'html.parser')
        
        for article in data1.find_all(class_='article__text'):
            itog = article.text.strip()
            #print(itog)
            output_file.write(itog)

        output_file.close()
        number += 1
except Exception as e:
    print(f"Error: {e}")