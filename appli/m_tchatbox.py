#!/usr/bin/env python
# -*- coding utf-8 -*-

import aiml
import os

# return tchatbox who learned and ready to go
def init():
    bot = aiml.Kernel()
    bot.setBotPredicate("name", "Jean-Paul")
    bot.learn(os.path.dirname(os.path.realpath(__file__))+os.path.sep+'std-startup.xml')
    bot.respond("load aiml b")
    return bot

# Get a question a return the Jean paul anwers
def robot_speak(bot, message):
    response = bot.respond(message)
    if response == '':
        return 'Parle a ma main'
    else:
        return response
