#!/usr/bin/env python3

import os
import argparse
import requests
from lxml import html
from tabulate import tabulate

URL = 'http://www3.olymp.vinnica.ua/cgi-bin/v_olymp/i2004/members4.py'
PATH = '/html/body/div/table/tr/td/table/tr[4]/td[3]/' \
'table/tr[2]/td/table/tr/td[2]/table/tr'

parser = argparse.ArgumentParser(
        description='Send problem to check')
parser.add_argument('--verbose', '-v', action='store_true',
        help='Verbose mode')
parser.add_argument('--source', '-s', required=True,
        help='Source to check')
parser.add_argument('--problem', '-p', required=True,
        help='Problem name')
parser.add_argument('--language', '-l',
        choices=['cpp', 'java', 'py'],
        help='Specify programming language')
parser.add_argument('--html',
        help='Save results in html')

args = parser.parse_args()

source = args.source
problem = args.problem
ext = os.path.splitext(source)[1]

def ext_to_lang(ext):
    if ext == '.py':
        return 'py3'
    elif ext == '.cpp':
        return 'cpp'
    elif ext == '.java':
        return 'java'
    elif ext == '.pas':
        return 'pas'

if args.language:
    language = args.language
else:
    language = ext_to_lang(ext)

if not args.verbose:
    print('Source: ', source)
    print('Problem: ', problem)
    print('Language: ', language)

data = {
        'problem': problem,
        'planguage': language,
        'language': 'ukr',
        'command': 'test',
        'code': 'pmg17',
}
files = {'source': open(source, 'rb')}

if not args.verbose:
    print('Sending request...')
r = requests.post(URL, data=data, files=files)
if not args.verbose:
    print('Response: ', r.status_code, r.reason)

if args.html:
    with open(args.html, 'w+') as out:
        out.write(r.text)

tree =  html.fromstring(r.content)
rows = tree.xpath(PATH)[1:] # First row contains th

table = []
for row in rows:
    num, res, time = [td.text for td in row[0:3]]
    time = time[:-2] # Remove ' c' at the end
    table.append([num, res, time])

print(tabulate(table, headers=['Number', 'Result', 'Time']))
