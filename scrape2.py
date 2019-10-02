import requests
from bs4 import BeautifulSoup

#url = "https://www.nporadio5.nl/gedraaid?show=112&date=11-04-2019"
url = "https://www.nporadio5.nl/gedraaid?show=all&date=11-04-2019"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

artist, titel = [], []
uls = soup.find_all('ul', class_="columns-3")

for ul in uls:
    h5s = ul.find_all('h5', class_="fn-artist")
    ps  = ul.find_all('p', class_="fn-song")
    for h5 in h5s:
        artist.append(h5.text)
    for p in ps:
        titel.append(p.text)

songs = zip(artist, titel)

for song in songs:
    a_song = "{0} - {1}".format(song[0], song[1])
    print(a_song)
