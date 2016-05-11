from django.conf.urls import patterns, include, url
from django.contrib import admin
from clubs.views import ClubListView, FixturesListView, matchmaking, match_results, functest
from django.contrib.auth.decorators import login_required as auth
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Elo_System.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'clubs.views.home', name='home'),
    url(r'^standings/$', ClubListView.as_view(), name='standings'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
#    url(r'^clubs/fixtures/$', auth( FixturesListView.as_view()), name='fixtures'),
    url(r'^fixtures/$', 'clubs.views.functest', name='fixtures'),
    url(r'^fixtures/match/$', 'clubs.views.game_session', name='match'),
    url(r'^fixtures/match/result/$', 'clubs.views.match_results', name='result'),
    url(r'^fixtures/session/$', 'clubs.views.game_session', name='session'),
    url(r'^clubs/calcultor/(?P<player_1_id>[a-zA-Z_ ]+)-(?P<player_2_id>[a-zA-Z_ ]+)/$', 'clubs.views.match_results', name="calculator")
) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
