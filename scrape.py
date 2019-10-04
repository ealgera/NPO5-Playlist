import requests
from bs4 import BeautifulSoup

#url = "https://www.nporadio5.nl/gedraaid?show=all&date=27-09-2019"
url_base = "https://www.nporadio5.nl/gedraaid?show=all&date="

song_80s = []

# Verwerk alle URL's van een week.
for i in range(23, 28):
    url = url_base + str(i) + "-09-2019"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    for a_div in soup.find_all("div", class_="card__content"):
        artist = a_div.find("p", class_="fn-artist truncate").text
        song   = a_div.find("p", class_="fn-song truncate").text
        song_80s.append(f"{artist} - {song}")

# Haal de dubbele songs eruit.
seen = []
for song in sorted(song_80s):
    if song not in seen:
        seen.append(song)
        print(song)
