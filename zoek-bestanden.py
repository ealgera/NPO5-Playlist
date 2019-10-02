import os
from pathlib import Path


bestand = "npo5-week70.txt"

# Maak vanuit de TXT een lijst met <artiest> - <titel>
line_count = 0

with open(bestand) as txt_file:
    new_songs = txt_file.read().splitlines()

'''
Per flac bestand:
   zet de bestandsnaam exclusief .flac in een lijst 'top2000'
Per song uit de new_songs:
   zoek de song in de lijst 'top2000'
   als gevonden:  
       print gevonden bestand.
   anders:
       splits song in artiest en titel
       zoek artiest in bestanden
'''

not_found, found = 0, 0
dir_name = "found_files/"
top2000 = []

path = Path('.').glob('*.flac')
for f in sorted(path):
    t = f.name.split(' - ') #[0]
    nr_t2000 = t[0]
    song = t[1] + ' - ' + t[2][:-5] # Exlusief extensie .flac

    song_t2000 = (nr_t2000, song)   
    top2000.append(song_t2000)      # top2000 is een lijst met tuples: (<nummer>, <song>)

found_list = [nr_2000 for song in new_songs for nr_2000 in top2000 if song in nr_2000]

print("Resultaat:")
print("Aantal te zoeken: {0}".format(len(new_songs)))
print("Aantal gevonden : {0}".format(len(found_list)))
