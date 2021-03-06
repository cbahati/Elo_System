#!/usr/bin/python 
from __future__ import division
import math

def foobar():
    print "IT WORKS!"

def expected_points( rating ):
    points = 1 - (1 / ( 1 + 10 ** (rating/400)))
    return points

def odds_of_winning(rating_1, rating_2):

    winner = rating_1
    loser = rating_2
   
    if winner > loser:
        topdog = winner
        underdog = loser
    else:
        underdog = winner
        topdog = loser

    rating_difference = abs(winner - loser)
    topdog_expected_pts = expected_points( rating_difference )
    underdog_expected_pts = (1 - topdog_expected_pts) 
    player_1_odds = int(underdog_expected_pts * 100)
    player_2_odds = int(topdog_expected_pts * 100)
    
    odds = (player_1_odds,player_2_odds)
  
    return odds


def elo_calc( winner, loser, result):
    
    if winner > loser:
        topdog = winner
        underdog = loser
    else:
        underdog = winner
        topdog = loser

    rating_difference = abs(winner - loser)
    topdog_expected_pts = expected_points( rating_difference )
    underdog_expected_pts = 1 - topdog_expected_pts
    

    if result == 0:
        points_gained = (30 *  ( .5 - topdog_expected_pts))
        points_lost = (30 *  ( .5 - underdog_expected_pts))
        print points_gained
        print points_lost

    elif winner > loser:
        points_gained = (30 *  ( 1 - topdog_expected_pts))
        points_lost = (30 *  ( 0 - underdog_expected_pts))
    else:
        points_gained = (30 *  ( 1 - underdog_expected_pts))
        points_lost = (30 *  ( 0 - topdog_expected_pts))

    winner_new_rating = winner + int(points_gained)
    loser_new_rating = loser + int(points_lost)
    if result == 0:
        new_ratings = (loser_new_rating, winner_new_rating)
        return new_ratings
    else:
        new_ratings = (winner_new_rating, loser_new_rating)
        return new_ratings
