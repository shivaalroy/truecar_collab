import sys

with open(sys.argv[1]) as f:
	lines = f.readlines();
	classifications = set();
	for row in lines:
		entry = row.split('\t')
		if (len(entry) > 3):
			classifications.add(entry[4])

print(classifications)
