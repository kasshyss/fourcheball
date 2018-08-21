#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
import bs4
import json
import requests
import m_conf as conf
import logging

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger('fourcheball')
logger.setLevel(logging.DEBUG)
logger.info('Init OK')

# Init
app_conf = conf.get_conf('back_end.conf')
@app.route('/')
def index():
    return 'Index available services :\n    - /fourcheball_end_point/serv_L1/ranking_L1'

# this url return L1 current ranking
@app.route('/fourcheball_end_point/serv_L1/ranking_L1')
def ranking_l1():
    logger.info('Get L1 ranking : new demand')
    # Set up client url
    logger.info('Get L1 ranking : grab data from website')
    url = app_conf['web_site'] + app_conf['web_target'] 
    # get html data
    resp = requests.get(url)
    logger.info('Get L1 ranking : parse html')
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    # get ranking tab
    ranking = soup.find('tbody')
    logger.info('Get L1 ranking : set up return')
    l1_result = {}
    i=0
    # for each row get the rank and the club name   
    for raw in ranking.find_all('tr', class_='standing-table__row'):
        l1_result[i+1] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]
        i=i+1
    logger.debug('return dico')
    return json.dumps(l1_result, ensure_ascii=False)

@app.route('/fourcheball_end_point/serv_L1/ranking_player')
def ranking_player():
    print 'TBD PLAYER RANKING'
