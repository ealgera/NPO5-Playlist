#bestand_80s  = "npo5-week80.txt"
bestand_80s  = "gevonden.txt"
bestand_2000 = "Top2000-2018-sorted.txt"

# Maak vanuit de TXT een lijst met <artiest> - <titel>
line_count = 0

with open(bestand_80s) as txt_file:
    top80s = [line.strip() for line in txt_file]

with open(bestand_2000) as txt_file:
    top2000 = [line.strip() for line in txt_file]

'''
Per top80s song:
    zoek de song in de lijst 'top2000'
    als gevonden:  
       print gevonden bestand.
    anders:
       print bestand niet gevonden.
'''

found_list = [nr_2000 for song in top80s for nr_2000 in top2000 if song in nr_2000]

print("Resultaat:")
print("Aantal te zoeken: {0}".format(len(top80s)))
print("Aantal gevonden : {0}".format(len(found_list)))
print()
for song in found_list:
    print(song)
