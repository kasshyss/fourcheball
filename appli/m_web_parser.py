#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Parse web site and get relevant data


class l1_web_parser:

    def __init__(self, target_url, l1_ranking_target):
        self.url = target_url
        self.ranking_target = l1_ranking_target

    def get_l1_ranking():
        # Set up client
        conn = http.client.HTTPSConnection(self.url)
        con.request('GET', ranking_target)
        # get data
        resp = conn.getresponse()
        soup = bs4.BeautifulSoup(resp.read(), 'html.parser')
        
