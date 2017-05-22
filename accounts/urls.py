from django.conf.urls import url

from accounts.views import *

urlpatterns = [
    url(r'^comments/', CommentView.as_view()),
    url(r'^relationships/', RelationshipView.as_view()),
    url(r'^feed/', FeedView.as_view()),
]
