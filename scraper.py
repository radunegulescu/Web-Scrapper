import requests
from bs4 import BeautifulSoup
import string
import os

os.chdir('D:/Web Scraper/Web Scraper/task')
n_pages = int(input())
topic = input()
url = 'https://www.nature.com/nature/articles'
for j in range(1, n_pages + 1):
    os.mkdir('Page_' + str(j))
    response = requests.get('https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page='+str(j), headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response:
        page_content = response.content
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        articles2 = []
        for x in articles:
            if x.find('span', {'class': 'c-meta__type'}).text == topic:
                name1 = x.find('a').text
                name = x.find('a').text
                for i in string.punctuation:
                    name1 = name1.replace(i, '')
                name2 = name1.maketrans(' ', '_')
                name1 = name1.translate(name2)
                name1 = name1.strip()
                name1 += '.txt'
                file = open('Page_' + str(j) + "/" + name1, 'w', encoding='utf-8')
                url2 = x.find('a', {'data-track-action': 'view article'})['href']
                url2 = 'https://www.nature.com' + url2
                response2 = requests.get(url2)
                print(url2)
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                body = soup2.find("article").text.strip()
                articles2.append(name1)
                file.write(body)
        print(articles2)
    else:
        print('The URL returned', str(response.status_code) + "!")
