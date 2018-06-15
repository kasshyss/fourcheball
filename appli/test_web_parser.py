#!/user/bien/env python
# -*- coding: utf-8 -*-

import m_web_parser as parser
import m_conf as conf

w_site = conf.get_conf('app.conf')['site']
target = conf.get_conf('app.conf')['target']


print(parser.get_l1_ranking(w_site, target))

