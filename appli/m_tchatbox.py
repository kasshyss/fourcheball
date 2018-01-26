#!/usr/bin/env python
# -*- coding utf-8 -*-

import aiml

# return tchatbox who learned and ready to go
def init():
    bot = aiml.Kernel()
    bot.learn("std-startup.xml")
    bot.respond("load aiml b")
    return bot

# Get a question a return the Jean paul anwers
def robot_speak(bot, message):
    return bot.respond(message)
