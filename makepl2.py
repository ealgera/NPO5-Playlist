from plexapi.server import PlexServer

plexurl = 'http://192.168.10.14:32400'
token = '3nWE3aqTEaYsnqvz6tky'
myTracks = []
plTracks = []
notFound = []

def zoekTracks(bieb, tracknaam, artiestnaam):
    list_found = []
    all_nrs = plex.library.section(bieb).searchTracks(title=tracknaam)  # Zoek alles wat lijkt op [tracknaam] in [bieb]
    subset_nrs = [x for x in all_nrs if x.originalTitle == artiestnaam] # Selecteer alleen de juiste [tracknamen]
    if len(subset_nrs) > 0:
        for nr in subset_nrs:
            if (artiestnaam in nr.originalTitle) and len(list_found) == 0: # We hoeven maar 1 te vinden...
                list_found.append(nr)
    return list_found      

def print_tracks(tracks):
    print("originalTitle - Title - Artist - Album")
    for track in tracks:
        print(track.originalTitle, " + ", track.title, " + ", track.artist(), " + ", track.album())
    print()

plex = PlexServer(plexurl, token)

#bestand_in = r"./lijst.txt"
bestand_in = r"./npo5-week70.txt"
counter = 0

with open(bestand_in, "r") as f:
    lines = f.readlines()

songs = [line.rstrip("\n") for line in lines]

for song in songs:
    #pos1 = song.find(" ")      # Zoek eerste spatie
    #pos2 = song.rfind("(")     # Zoek eerste ( vanaf de rechterkant
    #positie = song[0:pos1].strip() # Nummer, positie in lijst
    #naam = song[pos1:pos2].strip().split(" - ") # Lijst met titel en artiest
    naam = song.split(" - ")
    #jaar = song[pos2:].strip() # Jaar van de 'song' 
    
    nr_naam = naam[1]
    nr_artiest = naam[0]

    #print("Zoeken: {0}, {1}".format(nr_naam, nr_artiest))

    myTracks = zoekTracks('QNAPVarious', nr_naam, nr_artiest)
    if len(myTracks) == 0:
        myTracks = zoekTracks('QNAPMusic', nr_naam, nr_artiest)
        if len(myTracks) == 0:
            #print("\tDefinitief niet gevonden: {0} - {1}".format(nr_naam, nr_artiest))
            notFound.append(nr_artiest + " - " + nr_naam)
            continue
   
    plTracks.append(myTracks[0])

for playlist in plex.playlists():
    if playlist.title == "NPO5 Jaren 70":
        playlist.addItems(plTracks)
        print("Playlist aangepast...")

#new_pl = plex.createPlaylist("NPO5 Jaren 70", items=plTracks)
#print("Playlist created...")