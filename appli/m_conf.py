#!/usr/bin/env python

import os

#NOTE : conf file is two parts : Label|Value


def get_conf(file_name):

    try:
        file = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'conf' + os.path.sep + file_name, 'r')  
        lines = file.readlines()
        file.close()
    except ValueError:
        print 'Unable to open the log file ' + str(file_name) + str('\n')
    data = {}
    for line in lines:
        data[line.split('|')[0]] = line.split('|')[1][:-1:]
    return data
