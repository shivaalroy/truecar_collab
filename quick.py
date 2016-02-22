import csv

with open('clickstream/click_20150730.tsv','rb') as tsvin:
  file = csv.reader(tsvin, delimiter='\t')
  # csvout = csv.writer(csvout)

  count = -1
  for row in tsvin:
    count += 1
    if count == 0: continue
    # if count > 1000000: break
    entry = row.split("\t")
    entry[len(entry)-1] = entry[len(entry)-1][:-2]
    if entry[0] != "":
      print "\t".join(entry)
