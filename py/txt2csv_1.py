import csv

with open("clean.txt", encoding='utf-8') as f:
    
    x = f.readlines()
    s = []

    for i in x:
        s.append()
        print(s)

    csvex = csv.writer(open("txt2csv_exprt.csv", '', encoding='utf-8'), delimiter= ',',quoting=csv.QUOTE_ALL, dialect='excel')
    csvex.writerow(i)