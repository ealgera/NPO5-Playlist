from plexapi.server import PlexServer

plexurl = 'http://192.168.10.14:32400'
token = '3nWE3aqTEaYsnqvz6tky'
myTracks = []

def addTrack(n, t):
    myTracks.append(t)
    #print("Origineel: {0}, toegevoegd: {1}".format(n, t))

def print_tracks(level, tracks, tabs):
    tbs = "\t" * tabs
    level_str = "(Alles gevonden) "
    if not level:
        level_str = "(Subset gevonden) "
    print(tbs, level_str, " originalTitle - Title - Artist - Album")
    for track in tracks:
        print(tbs, track.originalTitle, " + ", track.title, " + ", track.artist(), " + ", track.album())

plex = PlexServer(plexurl, token)

bestand_in = r"./lijst2.txt"
counter = 0

with open(bestand_in, "r") as f:
    lines = f.readlines()

songs = [line.rstrip("\n") for line in lines]

for song in songs:
    pos1 = song.find(" ")
    pos2 = song.rfind("(")
    positie = song[0:pos1].strip()
    naam = song[pos1:pos2].strip().split(" - ")
    jaar = song[pos2:].strip()
    
    nr_naam = naam[0]
    nr_artiest = naam[1]
    gevonden = False
    print()
    print(nr_naam, "**", nr_artiest)
    print("======================")

    nummers = plex.library.section('QNAPVarious').searchTracks(title=nr_naam)
    print("--------Various-----------")
    print_tracks(1, nummers, 0)
    if len(nummers) == 0:
        print("*** Nummer {0} van {1} niet gevonden! {2}".format(nr_naam, nr_artiest, jaar))
        nummers2 = plex.library.section('QNAPMusic').searchTracks(title=nr_naam)
        t_list = [x for x in nummers2 if x.originalTitle == nr_artiest]
        print("--------Music-----------")        
        print_tracks(0, t_list, 1)
        #if len(nummers2) == 0:
        if len(t_list) == 0:
            counter += 1
            print("\t*** Nummer {0} van {1} definitief niet gevonden! {2}".format(nr_naam, nr_artiest, jaar))
        else:
            #for nummer in nummers2:
            for nummer in t_list:
                if not gevonden:
                    if nr_artiest in nummer.originalTitle:
                        print("\t", nr_naam, "-", nummer.title, " *** Toch gevonden, ", nummer.originalTitle, " --- ", (nummer.duration/60), nummer.media)
                        addTrack(nr_naam, nummer)  
                        gevonden = True  
    else:
        t_list = [x for x in nummers if x.originalTitle == nr_artiest]
        #print("**** t_list: ", t_list, " al gevonden...")
        print_tracks(0, t_list, 1)
        #for nummer in nummers:
        for nummer in t_list:
            if not gevonden:
                if nr_artiest in nummer.originalTitle:
                    print("Gevonden en toegevoegd: ", nr_naam, "-", nummer.title, " *** ", nummer.originalTitle, " --- ", (nummer.duration/60), nummer.media)
                    addTrack(nr_naam, nummer)
                    gevonden = True
                else:
                    print(">>> Niet Gevonden!! ", nr_naam, "-", nummer.title, " *** ", nummer.originalTitle)
                    nummers2 = plex.library.section('QNAPMusic').searchTracks(title=nr_naam)
                    t_list = [x for x in nummers2 if x.originalTitle == nr_artiest]
                    print("--------Music-----------")
                    print_tracks(0, t_list, 1)
                    #if len(nummers2) == 0:
                    if len(t_list) == 0:
                        counter += 1
                        print("\t*** Nummer {0} van {1} definitief niet gevonden! {2}".format(nr_naam, nr_artiest, jaar))
                    else:
                        #for nummer in nummers2:
                        for nummer in t_list:
                            if not gevonden:
                                if nr_artiest in nummer.originalTitle:
                                    print("\t", nr_naam, "-", nummer.title, " *** Toch gevonden, ", nummer.originalTitle, " --- ", (nummer.duration/60), nummer.media)
                                    addTrack(nr_naam, nummer)
                                    gevonden = True                    

print()
print("Totaal niet gevonden: {0}".format(counter))
print()
print("=============================")
for song in myTracks:
    print(song)

print()
print("Totaal aantal songs: {0}".format(len(myTracks)))

#new_pl = plex.createPlaylist("Test PL", items=myTracks)
#print("Playlist created...")
