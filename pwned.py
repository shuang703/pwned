#!/usr/bin/env python3.7
import csv

pwned = {}

with open('crap.csv', mode='w') as outfile:
  outfile_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  with open("pwned.tsv") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
      email = line[0]
      breach = line[1].split(',')
      for service in breach:
        print(email)
        print(service.lstrip())
        outfile_writer.writerow([email,service.lstrip()])
          
tsv.close()
outfile.close()

