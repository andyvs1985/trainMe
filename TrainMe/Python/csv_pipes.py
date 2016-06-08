import csv
import sys

csv.register_dialect('pipes', delimiter='|')

reader = csv.reader(sys.stdin, dialect='pipes')
for row in reader:
	print row