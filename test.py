from fuzzywuzzy import fuzz

# Check bestand op dubbele regels

#bestand_in = r"./npo5-week70.txt"
#
#with open(bestand_in, "r") as f:
#    #lines = f.readlines().strip("\n")
#    lines = [line.rstrip('\n') for line in f]
#
#count = 1
#sorted_lines = sorted(lines)
#
#line_old = sorted_lines[0]
#for line in sorted_lines[1:]:
#    count += 1
#    if line == line_old:
#        print("Dubbele gevonden: {0}".format(line))
#    line_old = line
#
#print("Bekeken regels: {0}".format(count))

# Controleer 2 bestanden op dubbele voorkomens

#bestand_1 = r"./npo5-week70.txt"
bestand_1 = r"./makepl2.txt"
bestand_2 = r"./Top2000-2018-sorted.txt"

with open(bestand_1, "r") as f:
    lines_1 = [line.rstrip('\n') for line in f]

with open(bestand_2, "r") as f:
    lines_2 = [line.rstrip('\n') for line in f]

sorted_lines_1 = sorted(lines_1) # NPO5
sorted_lines_2 = sorted(lines_2) # Top2000

# SET(A) - SET(B) = is gelijk aan de elementen in A maar niet in B.
# set_A.difference(set_B) voor (A - B)

diff = sorted(set(sorted_lines_1).difference(sorted_lines_2))  # Nummers wel in NPO5- maar niet in Top2000-lijst

count = 0
for d in diff:
    #zeker = [(i,fuzz.ratio(s, i)) for i in diff] # if 80 <= fuzz.ratio(s, i) <= 90]
    max_ratio = 0
    max_nr = ""
    for s in sorted_lines_2:
        f = fuzz.ratio(d, s)
        if f > max_ratio:
            max_ratio = f
            max_nr = s
    if max_ratio < 85:
        print("\tIn Diff: {0} en ({1}) - ({2})".format(d, max_nr, max_ratio))
    else:
        print("In Diff: {0} en ({1}) - ({2})".format(d, max_nr, max_ratio))

#    if len(zeker) > 0:
#        print("Zoeken  : {0}".format(s))
#        for nr in zeker:
#            count += 1
#            print("Gevonden: {0}".format(nr))
#        print()

print("Aantal gevonden: {0}".format(count))
