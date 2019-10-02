import requests
from bs4 import BeautifulSoup

#url = "https://www.nporadio5.nl/gedraaid?show=112&date=11-04-2019"
url = "https://www.nporadio5.nl/gedraaid?show=all&date=26-10-2019"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

#print(soup.prettify)

artist, titel = [], []
for h in soup.find('ul', class_="columns-3").parent.find_all('h5'):
    artist.append(h.text)

for p in soup.find('ul', class_="columns-3").parent.find_all('p', class_="fn-song"):
    titel.append(p.text)

print()
for song in zip(artist, titel):
    print(song[0], ' - ', song[1])


