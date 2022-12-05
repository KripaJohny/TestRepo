from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
 = soup.find('div', class_='article')

article =
print(soup)
ptint(article)

match = soup.title
print(match)

for article in soup .find_all('div', class_='article')
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_id)

vid_id = vid_src.split('/')[4]
print(vid_id)
