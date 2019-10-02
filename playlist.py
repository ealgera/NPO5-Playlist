from plexapi.server import PlexServer

plexurl = 'http://192.168.10.14:32400'
token = '3nWE3aqTEaYsnqvz6tky'

plex = PlexServer(plexurl, token)

#my_pl = plex.playlist("NPO5 70 Jaren")
#for song in my_pl.items():
#    print(song.title)

new_pl = plex.createPlaylist("Test PL", items=None)

print(type|(new_pl))

