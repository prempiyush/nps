from lxml import html
from bs4 import BeautifulSoup
import csv

def html2csv(htmlString, tableId):
    soup = BeautifulSoup(htmlString, "lxml")
    table = soup.find("table", id=tableId)
    #print(table)
    rows = []
    for row in table.find_all('tr'):
        rows.append([val.text for val in row.find_all('td')])
    return(rows)
