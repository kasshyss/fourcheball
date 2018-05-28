#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FB
from fbchat import Client
from fbchat.models import *

### Manage a faceboot tchat connection
# Get last message from a specified tchat
# Send a message to a tchat

class fb_client:

    def __init__(self, thread, login, password):
        self.client = Client(login, password)
        self.thread = thread
    
    # return the last message of a FB thread
    def get_last_message(self):
        return self.client.fetchThreadMessages(thread_id = self.thread, limit = 1)[0].text
    
    # Send a message to a FB thread
    def send_message(self, message):
        self.client.send(Message(text = message), thread_id = self.thread,  thread_type = ThreadType.GROUP)

    def __del__(self):
        self.client.logout()

