"""MoviewApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import *
from movies.views import *
from core.views import SearchView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^movies/[0-9]+/$', MovieDetailsView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', LoginView.as_view()),
    url(r'^users/', UserView.as_view()),
    url(r'^signup/', SignupView.as_view()),
    url(r'^search', SearchView.as_view()),
    url(r'^relationships/', RelationshipView.as_view()),
    url(r'^comments/', CommentView.as_view()),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
