#!/usr/bin/env python

import m_conf as conf

import http.client
import bs4

# init
web_site = conf.get_conf('app.conf')['site']
target = conf.get_conf('app.conf')['target']


l1_conn = http.client.HTTPSConnection(web_site)
l1_conn.request('GET', target)
resp = l1_conn.getresponse()
# parse anwers
soup = bs4.BeautifulSoup(resp.read(), 'html.parser')
# get ranking tab
ranking = soup.find('tbody')
l1_result = {}
# for each row get the rank and the club name   
for raw in ranking.find_all('tr', class_='standing-table__row'):
    l1_result[raw.find('td', class_='standing-table__cell standing-table__cell--position').contents[0]] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]


print l1_result
