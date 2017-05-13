import requests
import csv
from html2csv import html2csv

cookies = {
    '__utma': '26363680.772210374.1493554032.1493981988.1494126699.4',
    '__utmc': '26363680',
    '__utmz': '26363680.1493554090.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '__utmv': '26363680.|1=Theme=CleanPeppermintBlack=1',
    'd28269d451fcce41556504daac1f7b3a': '3ff3enktbqlp73t5o743i9vi22',
    'ext_name': 'jaehkpjddfdgiiefcnhahapilbejohhj',
}

headers = {
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://www.licpensionfund.in/index.php?option=com_content&view=article&id=47',
    'Connection': 'keep-alive',
}

schemes = ['Scheme1', 'Scheme2', 'Scheme3', 'Scheme4', 'lpfset1', 'lpfsct1', 'lpfsgt1', 'lpfsat1', 'lpfset2', 'lpfsct2', 'lpfsgt2', 'lpfsat2', 'lpfapys']

for scheme in schemes:
    print("Fetching details for " + scheme)
    writer = csv.writer(open("lic-"+scheme+".csv", "a"))
    params = {'Exchg': scheme}
    result = requests.get('http://www.licpensionfund.in/Navnew.php', headers=headers, params=params, cookies=cookies)
    rows = html2csv(result.text, '')
    for row in rows:
        if not row:
            continue
        writer.writerow(row)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.get('http://www.licpensionfund.in/Navnew.php?Exchg=Scheme1', headers=headers, cookies=cookies)
