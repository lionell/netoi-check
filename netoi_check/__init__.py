import os
import requests
from lxml import html as lhtml
from tabulate import tabulate

URL = 'https://www3.olymp.vinnica.ua/cgi-bin/v_olymp/i2004/members4.py'
PATH = '/html/body/div/table/tr/td/table/tr[4]/td[3]/' \
       'table/tr[2]/td/table/tr/td[2]/table/tr'

def ext_to_lang(ext):
    if ext == '.py':
        return 'py3'
    elif ext == '.cpp':
        return 'cpp'
    elif ext == '.cc':
        return 'cpp'
    elif ext == '.java':
        return 'java'
    elif ext == '.pas':
        return 'pas'

def check(problem, source, language, silent, html):
    if language is None:
        ext = os.path.splitext(source)[1]
        language = ext_to_lang(ext)

    if not silent:
        print('Source:   ', source)
        print('Problem:  ', problem)
        print('Language: ', language)

    data = {
            'problem': problem,
            'planguage': language,
            'language': 'ukr',
            'command': 'test',
            'code': 'pmg17',
    }
    files = {'source': open(source, 'rb')}

    if not silent:
        print('Sending request...')
    r = requests.post(URL, data=data, files=files)
    if not silent:
        print('Response: ', r.status_code, r.reason)

    if html is not None:
        with open(html, 'w+') as out:
            out.write(r.text) 
    tree =  lhtml.fromstring(r.content)
    rows = tree.xpath(PATH)[1:] # First row contains th

    table = []
    for row in rows:
        num, res, time = [td.text for td in row[0:3]]
        time = time[:-2] # Remove ' c' at the end
        table.append([num, res, time])

    return tabulate(table, headers=['Number', 'Result', 'Time'])
