#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask import request
import bs4
import json
import requests
import m_conf as conf
import logging
from fbchat import Client
from fbchat.models import *

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger('fourcheball')
logger.setLevel(logging.INFO)
app_conf = conf.get_conf('back_end.conf')
logger.info('Init OK')

@app.route('/')
def index():
    return 'Index available services :\n    - /fourcheball_end_point/serv_L1/ranking_L1\n       -/fourcheball_end_point/serv_fb/get_last_messages'

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

# return last 3 messages from a a fb conversation
@app.route('/fourcheball_end_point/serv_fb/get_last_messages')
def fb_messages():
    logger.info('Get last fb messages : init')
    fb_thread = int(app_conf['fb_thread'])
    fb_client = Client(app_conf['fb_login'],app_conf['fb_password'])
    logger.info('Get last fb messages : grab last messages')
    last_messages = fb_client.fetchThreadMessages(thread_id = fb_thread, limit = 3)
    msg = {} 
    msg[0] = last_messages[2].text
    msg[1] = last_messages[1].text
    msg[2] = last_messages[0].text
    logger.info('Get last fb messages : return result')
    return json.dumps(msg, ensure_ascii=False)

# send message to fb thread
@app.route('/fourcheball_end_point/serv_fb/send_msg', )
def send_fb_msg():
    logger.info('Send new message to fb')
    msg = request.args.get('msg')
    logger.info('Message : {}'.format(msg))
    fb_thread = int(app_conf['fb_thread'])
    fb_client = Client(app_conf['fb_login'],app_conf['fb_password'])
    fb_client.send(Message(text = msg), thread_id = fb_thread, thread_type = ThreadType.GROUP)
    logger.info('Message posted')
    return fb_messages()

# get player ranking from google spreadsheet
@app.route('/fourcheball_end_point/serv_L1/ranking_player')
def get_ranking_player():
    print 'TBD PLAYER RANKING'
