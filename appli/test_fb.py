#!/usr/bin/env python
# -*- coding utf-8 -*-

import m_conf as conf
import m_tchats as tchats

fb = conf.get_conf('fb.conf')

fb_tchat = tchats.fb_client(fb['thread'],fb['login'],fb['password'])
print fb_tchat.get_last_message()
