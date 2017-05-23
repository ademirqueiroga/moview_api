from django.conf.urls import url

from accounts.views import *

urlpatterns = [
    url(r'^comments/', CommentView.as_view()),
    url(r'^relationships/', RelationshipView.as_view()),
    url(r'^profile/$', ProfileView.as_view()),
    url(r'^favorites/$', FavoriteView.as_view()),
    url(r'^watchlist/$', WatchlistView.as_view()),
    #url(r'^profile/[0-9]+/$', ProfileView.as_view()),
]
