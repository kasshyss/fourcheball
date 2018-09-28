#!/usr/bin/env python

import os
import logging
import e_conf as c

logging.basicConfig()
logger = logging.getLogger('m_config')
logger.setLevel(c.logger_level.CURRENT_LEVEL.value)

def add_space(item, size):
    item_len = len(str(item))
    item = str(item)
    if item_len >= size:
        return item
    for i in range(size - item_len):
        item = ' ' + item
    return item

#NOTE : conf file is two parts : Label|Value
def get_conf(file_name):
    
    logger.debug('get_conf:Init function') 
    data = {}
    lines = []

    if isinstance(file_name, str) is False:
        logger.error('get_conf:Wrong parameter type, string is require.')
        logger.debug('get_conf:Exit function')
        return data

    try:
        logger.debug('get_conf:Fetch data from file {}'.format(file_name))
        file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'conf' + os.path.sep + file_name, 'r')  
        lines = file.readlines()
        file.close()
    except ValueError:
        logger.error('get_conf:Unable to open the log file {}'.format(file_name))
        logger.debug('get_conf:Exit function')
        return data
    if len(lines) != 0:
        logger.debug('get_conf:Organise conf in a dico')
        for line in lines:
            data[line.split('|')[0]] = line.split('|')[1][:-1:]
    
    logger.info('get_conf:Return conf for {}'.format(file_name))
    logger.debug('get_conf:Exit function')
    return data

# see google tutorial to generate credentials for the app
def get_google_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
   


