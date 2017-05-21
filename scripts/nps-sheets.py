import gspread
import requests
import zipfile
import os
import sys
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date, timedelta
from utils import csv2list

dateFormat = "%d%m%Y"
schemes = ('SM001001', 'SM001002', 'SM001003', 'SM001004', 'SM001005', 'SM001006', 'SM001007', 'SM001008', 'SM001009', 'SM001010', 'SM001011', 'SM001012', 'SM001013', 'SM002001', 'SM002002', 'SM002003', 'SM002004', 'SM002005', 'SM002006', 'SM002007', 'SM002008', 'SM002009', 'SM002010', 'SM002011', 'SM002012', 'SM002013', 'SM003001', 'SM003002', 'SM003003', 'SM003004', 'SM003005', 'SM003006', 'SM003007', 'SM003008', 'SM003009', 'SM003010', 'SM003011', 'SM003012', 'SM003013', 'SM005001', 'SM005002', 'SM005003', 'SM005004', 'SM005005', 'SM005006', 'SM005007', 'SM005008', 'SM005009', 'SM006001', 'SM006002', 'SM006003', 'SM006004', 'SM006005', 'SM006006', 'SM006007', 'SM006008', 'SM006009', 'SM007001', 'SM007002', 'SM007003', 'SM007004', 'SM007005', 'SM007006', 'SM007007', 'SM007008', 'SM007009', 'SM008001', 'SM008002', 'SM008003', 'SM008004', 'SM008005', 'SM008006', 'SM008007', 'SM008008', 'SM008009', 'SM010001', 'SM010002', 'SM010003', 'SM010004', 'SM010005', 'SM010006', 'SM010007', 'SM010008')

def outFileToFormattedRow(fileName):
    print("outFileToFormattedRow: Entering.. Have to format " + fileName)
    fileDate = datetime.strptime(fileName.split("_")[2].split(".")[0], dateFormat)
    rows = csv2list(fileName)

    # Sorting the rows based on the Scheme ID
    # A row is of the format:
    # ['05/02/2017', 'PFM008', 'HDFC PENSION MANAGEMENT COMPANY LIMITED', 'SM008009', 'HDFC PENSION MANAGEMENT COMPANY LIMITED SCHEME A - TIER II', '10.2628']
    rows.sort(key=lambda x: x[3])
    newRow = [''] * (len(schemes) + 1)

    for row in rows:
        firstCol = datetime.strptime(row[0], '%m/%d/%Y')
        if not firstCol == fileDate:
            print("outFileToFormattedRow: File for " + fileDate.strftime("%d/%m/%Y") + " has an entry for " + firstCol.strftime("%d/%m/%Y"))
            continue
        i = -1
        newRow[0] = fileDate.strftime('%d/%m/%Y')
        try:
            #print(row)
            i = schemes.index(row[3])
        except Exception as e:
            print("outFileToFormattedRow: No scheme id found. New Scheme?")
            # TODO needs more work. Perhaps email if this error?
        else:
            newRow[i + 1] = float(row[5])
    print("outFileToFormattedRow: Deleting file: " + fileName)
    os.remove(fileName)
    print("outFileToFormattedRow: Returning row: " + newRow)
    return(newRow)

def downloadDataFromNPS(fileDate):
    fileName = "NAV_File_"+fileDate.strftime(dateFormat)+".zip"
    print("downloadDataFromNPS: Entering.. Have to download " + fileName)

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
    }

    params = (
        ('path', 'download/'),
        ('filename', fileName),
    )

    result = requests.get('https://npscra.nsdl.co.in/download.php', headers=headers, params=params)

    if(result.content):
        print("downloadDataFromNPS: File " + fileName + " downloaded. Saving")
        zfile = open(fileName, 'wb')
        zfile.write(result.content)
        zfile.close()
        zip_ref = zipfile.ZipFile(fileName, 'r')
        print("downloadDataFromNPS: Extracting File " + fileName)
        zip_ref.extractall()
        outFile = zip_ref.namelist()[0]
        zip_ref.close()
        print("downloadDataFromNPS: Extracting File " + fileName)
        os.remove(fileName)
        print("downloadDataFromNPS: Returning " + outFile)
        return(outFile)
    print("downloadDataFromNPS: No data returned from NPS. Returning False")
    return(False)


def appendRow(endDate = ''):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key("1tW_q9iW8ltWqcACNj3QaDcq9R6WKZODlKHrbGrZCAAs").worksheet("Master")
    # Fetch a cell range
    #cell_list = wks.range('A1:B7')
    if(endDate):
        endDate = datetime.strptime(endDate, "%d/%m/%Y")
    else:
        endDate = date.today()
    rowCount = wks.row_count
    lastRow = wks.row_values(rowCount)
    lastDate = datetime.strptime(lastRow[0],"%d/%m/%Y")
    currentDate = lastDate + timedelta(1)
    while(currentDate <= endDate):
        fileName = downloadDataFromNPS(currentDate)
        if(fileName):
            values = outFileToFormattedRow(fileName)
        else:
            print("appendRow: No NAV on " + currentDate.strftime(dateFormat))
            print("appendRow: Using NAV from " + lastDate.strftime(dateFormat))
            values = lastRow
            values[0] = currentDate.strftime("%d/%m/%Y")
        wks.append_row(values)
        print("Values for " + currentDate + " updated")
        rowCount = rowCount + 1
        lastRow = values
        lastDate = currentDate
        currentDate = currentDate + 1

appendRow()
