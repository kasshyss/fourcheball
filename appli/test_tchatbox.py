#!/usr/bin/env python
# -*- coding utf-8 -*-

import m_tchatbox as robot

jean_paul = robot.init()
message = 'Bonjour'
while message != 'Je me casse':
    robot_say= robot.robot_speak(jean_paul, message)
    if robot_say == '':
        print 'lapincompris'
    else:
        print robot_say
    message = raw_input('Demande a Jean Paul : ')
