import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-d")
args = parser.parse_args()
import csv

dateDict = {}#dictionary contains dates of entries as keys, and a dictionary of occurences of each item for that day

with open(args.file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        date = row[1][:10]
        if date not in dateDict:
            dateDict[date] = {}
        if row[0] not in dateDict[date]:
            dateDict[date][row[0]] = 1
        else:
            dateDict[date][row[0]] += 1
#once dictionary is constructed, use dictionary to find max occurences of item on a single day and store in res
res = []
if args.d not in dateDict:
    print("date "+ args.d +" not found in " + args.file)
    exit()

max = max(dateDict[args.d].values()) #number of occurences of highest occurence item on given date
for item in dateDict[args.d]:
    if dateDict[args.d][item] == max:
        res.append(item)
#print res
for val in res:
    print(val)





