#import csv
#import os
#from pathlib import Path

bestand = "lijst2018.txt"

with open(bestand) as txtfile:
    temp = txtfile.read().splitlines()
    line_count = 0
    for line in temp[500:1000]:
        line_count += 1
        #line = '9999 - ' + line
        fn = open(line,"w")
        fn.write(" ")
        fn.close()
        #print(line)
    print("Totaal: {0}".format(line_count))

