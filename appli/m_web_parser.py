#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Parse web site and get relevant data


# Parse a web page to get French Ligue 1
# return : dico[rank]=team name
def get_l1_ranking(target_url, l1_ranking_target):
    # Set up client
    conn = http.client.HTTPSConnection(self.url)
    con.request('GET', ranking_target)
    # get data
    resp = conn.getresponse()
    soup = bs4.BeautifulSoup(resp.read(), 'html.parser')
        
    # get ranking tab
    ranking = soup.find('tbody')
    l1_result = {}
    # for each row get the rank and the club name   
    for raw in ranking.find_all('tr', class_='standing-table__row'):
        l1_result[int(raw.find('td', class_='standing-table__cell standing-table__cell--position').contents[0])] = raw.find('td', class_='standing-table__cell standing-table__cell--team').find('span', class_='text').contents[0]

    return l1_result
