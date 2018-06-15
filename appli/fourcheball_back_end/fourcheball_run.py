#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
import bs4
import json
import requests
import m_conf as conf

app = Flask(__name__)

app_conf = conf.get_conf('back_end.conf')

@app.route('/fourcheball_end_point/serv_L1/')
def toto():
    print 'toto'




@app.route('/fourcheball_end_point/serv_L1/ranking_L1')
def ranking_l1():
    # Set up client
    url = app_conf['web_site'] + app_conf['web_target'] 
    # get data
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    # get ranking tab
    ranking = soup.find('tbody')
    l1_result = {}
    # for each row get the rank and the club name   
    for raw in ranking.find_all('tr', class_='standing-table__row'):
        l1_result[int(raw.find('td', class_='standing-table__cell standing-table__cell--position').contents[0])] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]
    print l1_result
    return json.dumps(l1_result, ensure_ascii=False)


@app.route('/fourcheball_end_point/serv_L1/ranking_player')
def ranking_player():
    print 'TBD PLAYER RANKING'
