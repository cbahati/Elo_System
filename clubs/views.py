from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Club
from .forms import Play_Match
from django.core.urlresolvers import reverse, reverse_lazy
from elo_calculator import foobar
from match import make_fixtures
from elo_calculator import *
from django.contrib.auth.decorators import login_required
# Create your views here.


class ClubListView(ListView):
    model = Club
    
class FixturesListView(ListView):
    template_name = "fixtures.html"
    model = Club

def home(request):
    return render(request, 'home.html',{} )
    
def matchmaking():
    clubs = Club.objects.all()
    
    new_rank = 1

    for team in clubs:        

        team.last_rank = team.rank
        team.rank = new_rank
        last_rank = team.last_rank

        if new_rank != last_rank:
            rank_difference = new_rank - last_rank
            if rank_difference > 0:
                team.rank_difference = "-" + str(rank_difference)
            else:
                team.rank_difference = "+" + str(abs(rank_difference))
        else:
            team.rank_difference = "-"
            
        team.save()
        new_rank = new_rank + 1
        
   # return render(request, 'fixtures.html',{} )

@login_required
def match_results(request, player_1_id, player_2_id):
    form = Play_Match(request.POST)
    player_1 = Club.objects.get(club_name = player_1_id)
    player_2 = Club.objects.get(club_name = player_2_id)
    player_1_item = {}
    player_2_item = {}
    odds = odds_of_winning(player_1.rank_score, player_2.rank_score)

    if odds[0] > odds[1]:
        favorite = odds[0]
        underdog = odds[1]
    else:
        favorite = odds[1]
        underdog = odds[0]
    
    if player_1.rank_score > player_2.rank_score:
        player_1_item['odds'] = favorite
        player_2_item['odds'] = underdog
        player_1_item['club_info'] = player_1
        player_2_item['club_info'] = player_2
    else:
        player_1_item['odds'] = underdog
        player_2_item['odds'] = favorite
        player_1_item['club_info'] = player_1
        player_2_item['club_info'] = player_2

    context = {
        "form":form,
        'player_1':player_1_item,
        'player_2':player_2_item,
    }

    if form.is_valid():
        player_1_score = form.cleaned_data['player_1']
        player_2_score = form.cleaned_data['player_2']
        print player_1_score
        print player_2_score

        if player_1_score > player_2_score:
            winner = player_1
            loser = player_2
            winner_goals = player_1_score
            winner_rating = winner.rank_score
            loser_rating = loser.rank_score
            loser_goals = player_2_score
            result = 1
        elif player_1_score < player_2_score:
            winner = player_2
            winner_goals = player_2_score
            loser = player_1
            winner_rating = player_2.rank_score
            loser_goals = player_1_score
            loser_rating = player_1.rank_score
            result = 1

        else:
            print "tie"
      
            if player_1_score > player_2_score:
                winner = player_2
                loser = player_1
                print "poop"
                winner_rating = player_2.rank_score
                loser_rating = player_1.rank_score
                result = 0
            else:
                winner = player_1
                loser = player_2
                print "doop"
                winner_rating = player_1.rank_score
                loser_rating = player_2.rank_score
                result = 0




        new_ratings = elo_calc(winner_rating, loser_rating, result)

        points_gained = new_ratings[0] - winner.rank_score
        points_lost = loser.rank_score - new_ratings[1]

        winner.rank_score = new_ratings[0]
        winner.wins = winner.wins + 1
        winner.goal_for += winner_goals
        winner.goal_against += loser_goals
        winner.goal_difference = winner.goal_for - winner.goal_against
        winner.save()

        loser.rank_score = new_ratings[1]
        loser.loss = loser.loss + 1
        loser.goal_for += loser_goals
        loser.goal_against += winner_goals
        loser.goal_difference = loser.goal_for - loser.goal_against
        loser.save()
        
        for key, item in request.session.iteritems():
            if type(item) == list:
                if winner.club_name in item and loser.club_name in item:
                    del request.session[key]
                    request.session.modified = True
                    print "DONE"
                    break

        matchmaking()
        
        result_player_1 = {}
        result_player_2 = {}

        result_player_1['club_info'] = winner
        result_player_1['points_gained'] = points_gained

        result_player_2['club_info'] = loser
        result_player_2['points_lost'] = points_lost
        poop = 99999
        
        context = {
            'player_1':result_player_1,
            'player_2':result_player_2,
            'poop':poop
        }

        return render(request, 'points.html', context)


    return render(request, 'result.html', context )


@login_required
def game_session(request):

    clubs = Club.objects.all()
    club_list = {}

    for team in clubs:
        club_list[team.club_name] = team.rank_score
        fixtures = make_fixtures(club_list)

    for count, games in enumerate(fixtures):
        request.session[str(count)] = games
    
    games = []
    for item in request.session.itervalues():
        if type(item) == list:
            game = (item[0], item[1])
            games.append(game)
 
    context = {
        "fixtures": games
    }

    return render(request, 'fixtures.html', context)
 

@login_required
def functest(request):
    
    fixtures = []
    for item in request.session.itervalues():
        if type(item) == list:
            game = (item[0], item[1])
            fixtures.append(game)
    context = {
        "fixtures": fixtures
    }
    
    return render(request, 'fixtures.html', context )
