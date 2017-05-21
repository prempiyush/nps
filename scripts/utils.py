import csv


def csv2list(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        data = f.read()
        new_data = data.replace('"', '')
        rows = []
        for row in csv.reader(new_data.splitlines(), delimiter=',', skipinitialspace=True):
            rows.append(row)
        return(rows)
