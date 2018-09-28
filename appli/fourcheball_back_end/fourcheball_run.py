#!usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
from flask import request
import bs4
import json
import requests
import m_conf as conf
import e_conf as c
import logging
from fbchat import Client
from fbchat.models import *

app = Flask(__name__)
logging.basicConfig()
logger = logging.getLogger('fourcheball')
logger.setLevel(c.logger_level.CURRENT_LEVEL.value)
app_conf = conf.get_conf('back_end.conf')
logger.info('fourcheball_run:Init done')

@app.route('/')
def index():
    return 'Index available services :\n    - /fourcheball_end_point/serv_L1/ranking_L1\n       -/fourcheball_end_point/serv_fb/get_last_messages'

# this url return L1 current ranking
@app.route('/fourcheball_end_point/serv_L1/ranking_L1')
def ranking_l1():
    logger.debug('ranking_l1:Init function')
    # Set up client url
    web_site = app_conf['web_site'] 
    web_target = app_conf['web_target']
    url = web_site + web_target
    l1_result={}
    i = 0

    try:
        logger.debug('ranking_l1:Fetch data from target {}'.format(url))
        resp = requests.get(url)
        logger.debug('ranking_l1:Parse HTML')
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        # get ranking tab
        ranking = soup.find('tbody')
        logger.debug('ranking_l1:Prepare output')
        # for each row get the rank and the club name   
        for raw in ranking.find_all('tr', class_='standing-table__row'):
            l1_result[i+1] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]
            i = i+1
        logger.info('ranking_l1:L1 ranking fetched')
    except ValueError:
        logger.error('ranking_l1:Fail to fetch L1 ranking on {}'.format(web_site))
    logger.debug('ranking_l1:Exit function')
    return json.dumps(l1_result, ensure_ascii=False)

# return last 3 messages from a a fb conversation
@app.route('/fourcheball_end_point/serv_fb/get_last_messages')
def fb_messages():
    logger.debug('fb_messages:Init function')
    msg = {}
    msg[0] = ''
    msg[1] = ''
    msg[2] = ''

    try:
        logger.debug('fb_messages:Init channel')
        fb_thread = int(app_conf['fb_thread'])
        fb_client = Client(app_conf['fb_login'],app_conf['fb_password'])
        logger.debug('fb_messages:Fetch last 3 messages')
        last_messages = fb_client.fetchThreadMessages(thread_id = fb_thread, limit = 3)
        msg[0] = last_messages[2].text
        msg[1] = last_messages[1].text
        msg[2] = last_messages[0].text
        logger.info('fb:messages:Messages fetched from thread {}'.format(fb_thread))
    except ValueError:
        logger.error('fb_messages:Fail to reach fb messages')
    
    logger.debug('fb_messages:Exit function')
    return json.dumps(msg, ensure_ascii=False)

# send message to fb thread
@app.route('/fourcheball_end_point/serv_fb/send_msg', )
def send_fb_msg():
    logger.debug('send_fb_msg:Init function')
    msg = ''
    fb_thread = int(app_conf['fb_thread'])
    try:
        msg = request.args.get('msg')
        logger.debug('send_fb_msg:New message : {}'.format(msg))
        fb_client = Client(app_conf['fb_login'],app_conf['fb_password'])
        logger.debug('send_fb_msg:Send message')
        fb_client.send(Message(text = msg), thread_id = fb_thread, thread_type = ThreadType.GROUP)
        logger.info('send_fb_msg:Message posted on facebook')
    except ValueError:
        logger.error('send_fb_msg:Fail to post message in thread {}'.format(fb_thread))
    logger.debug('send_fb_msg:Exit function')
    return fb_messages()

# get player ranking from google spreadsheet
@app.route('/fourcheball_end_point/serv_L1/ranking_player')
def get_ranking_player():
    print 'TBD PLAYER RANKING'
