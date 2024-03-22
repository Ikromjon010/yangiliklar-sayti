
from django.contrib import admin
from django.urls import path, include
from .views import news_list_view, NewsListView, news_detail_view, sport_news_list_view

urlpatterns = [
    path('all/', news_list_view, name = 'news_list_page' ),
    path('sport/', sport_news_list_view, name = 'sport_news_page' ),
    # path('all/', NewsListView.as_view(), name = 'news_list_page' ),
    path('<int:id>/', news_detail_view, name = 'news_detail_page' ),
]
