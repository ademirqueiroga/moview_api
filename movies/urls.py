from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from movies.views import *

router = DefaultRouter()
router.register(r'^categories', CategoryViewSet)
router.register(r'', MovieViewSet) # NEED TO BE THE LAST ROUTE

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^comments/$', CommentView.as_view()),
    url(r'^details/[0-9]+/$', MovieDetailsView.as_view()),
]
