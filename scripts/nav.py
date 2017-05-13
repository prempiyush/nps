import requests
from datetime import date
from zipfile import ZipFile
from io import BytesIO
from tqdm import tqdm

cookies = {
    'PHPSESSID': '73nrq77aqum1bgmr5uvt1qrcp7',
    'ext_name': 'jaehkpjddfdgiiefcnhahapilbejohhj',
}

headers = {
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

today = date.today().strftime("%d%m%Y")

params = (
    ('path', 'download/'),
    ('filename', 'NAV_File_' + today + '.zip'),
)

result = requests.get('https://npscra.nsdl.co.in/download.php', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.get('https://npscra.nsdl.co.in/download.php?path=download/&filename=NAV_File_27042017.zip', headers=headers)

if(result.status_code == requests.codes.ok):
    # do something
    print(result.headers)
    print(result.request.headers)
    print(result.raw.read(10))
    with open("10MB", "wb") as handle:
        for data in tqdm(result.iter_content()):
            handle.write(data)
else:
    print(result)
