bestand_in = r"./lijst.txt"

with open(bestand_in, "r") as f:
    lines = f.readlines()

songs = [line.rstrip("\n") for line in lines]

for song in songs:
    pos1 = song.find(" ")
    pos2 = song.rfind("(")
    positie = song[0:pos1].strip()
    naam = song[pos1:pos2].strip()
    #print(naam)
    naam = naam.split("-")
    #print(naam)
    jaar = song[pos2:].strip()
    if len(naam) < 2:
        print(naam)

