#!/usr/bin/env python
# -*- coding: utf-8 -*-

import m_conf as conf

import http.client
import bs4

from googleapiclient import discovery
from pprint import pprint
import httplib2

from fbchat import Client
from fbchat.models import *

# init
web_site = conf.get_conf('app.conf')['site']
target = conf.get_conf('app.conf')['target']
spreadsheet_target = conf.get_conf('app.conf')['spreadsheet']
spreadsheet_range = conf.get_conf('app.conf')['range']
spreadsheet_value_input_option = conf.get_conf('app.conf')['value_input_option']
spreadsheet_data_input_option = conf.get_conf('app.conf')['data_input_option']
spreadsheet_result = conf.get_conf('app.conf')['result_range']

credentials = conf.get_google_credentials()
c_http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
service = discovery.build('sheets', 'v4', http = c_http, discoveryServiceUrl=discoveryUrl)


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
    l1_result[int(raw.find('td', class_='standing-table__cell standing-table__cell--position').contents[0])] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]
# Connect to fourcheball spreatsheet

values = [
            [l1_result[1]]
            ,[l1_result[2]]
            ,[l1_result[3]]
            ,[l1_result[4]]
            ,[l1_result[5]]
            ,[l1_result[6]]
            ,[l1_result[7]]
            ,[l1_result[8]]
            ,[l1_result[9]]
            ,[l1_result[10]]
            ,[l1_result[11]]
            ,[l1_result[12]]
            ,[l1_result[13]]
            ,[l1_result[14]]
            ,[l1_result[15]]
            ,[l1_result[16]]
            ,[l1_result[17]]
            ,[l1_result[18]]
            ,[l1_result[19]]
            ,[l1_result[20]]
        ]
body = {
        'values' : values
        }

service.spreadsheets().values().update(spreadsheetId = spreadsheet_target, range=spreadsheet_range, valueInputOption = spreadsheet_value_input_option,body = body).execute()
# get score
result = service.spreadsheets().values().get(spreadsheetId = spreadsheet_target, range=spreadsheet_result).execute()
fourcheball_result = 'Fourcheballer   Point   Rang\n'
for item in  result['values']:
    fourcheball_result = fourcheball_result + conf.add_space(item[0], 13) + '   ' + conf.add_space(item[1], 5) + '   ' + conf.add_space(item[2], 4) + '\n'

print fourcheball_result

fb_client = Client(conf.get_conf('app.conf')['fb_login'], conf.get_conf('app.conf')['fb_pass'])
#fb_client.send(Message(text = 'Salut les nazes, c\'est l\'heure du classement'), thread_id=int(conf.get_conf('app.conf')['fb_message_id']), thread_type=ThreadType.GROUP)
#fb_client.send(Message(text = fourcheball_result), thread_id=int(conf.get_conf('app.conf')['fb_message_id']), thread_type=ThreadType.GROUP)
fb_client.logout()

