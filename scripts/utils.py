import csv


def csv2list(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return(rows)
