#!/usr/bin/python
from itertools import combinations
from random import shuffle
  
def make_fixtures(teams):

    group_1 = {}
    group_2 = {}
    group_3 = {}
    group_4 = {}
    group_5 = {}
    group_6 = {}

    for club_name, rating in teams.iteritems():
        if rating < 1000:
            group_6[club_name] = rating
        elif rating >= 1000 and rating <= 1200:
            group_5[club_name] = rating
        elif rating > 1200 and rating <= 1400:
            group_4[club_name] = rating
        elif rating > 1400 and rating <= 1600:
            group_3[club_name] = rating
        elif rating > 1600 and rating <= 1800:
            group_2[club_name] = rating
        else:
            group_1[club_name] = rating

    if len(group_6) < 5:
        temp = group_6.copy()
        group_6 = {}
        group_5.update(temp)

    if len(group_5) < 5:
        temp = group_5.copy()
        group_5 = {}
        group_4.update(temp)

    if len(group_4) < 5:
        temp = group_4.copy()
        group_4 = {}
        group_3.update(temp)

    if len(group_3) < 5:
        temp = group_3.copy()
        group_3 = {}
        group_2.update(temp)

    if len(group_2) < 5 or len(group_1) < 5:
        temp = group_2.copy()
        group_2 = {}
        group_1.update(temp)
    
    
    group_1_fixtures = combinations(group_1, 2)
    group_2_fixtures = combinations(group_2, 2)
    group_3_fixtures = combinations(group_3, 2)
    group_4_fixtures = combinations(group_4, 2)
    group_5_fixtures = combinations(group_5, 2)
    group_6_fixtures = combinations(group_6, 2)

    fixtures_list = []
    
    for games in group_1_fixtures:
        fixtures_list.append(games)
    
    for games in group_2_fixtures:
        fixtures_list.append(games)

    for games in group_3_fixtures:
        fixtures_list.append(games)
    
    for games in group_4_fixtures:
        fixtures_list.append(games)

    for games in group_5_fixtures:
        fixtures_list.append(games)

    for games in group_6_fixtures:
        fixtures_list.append(games)

        
    shuffle(fixtures_list)
    
    return fixtures_list
