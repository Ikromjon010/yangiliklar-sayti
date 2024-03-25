
from django.contrib import admin
from django.urls import path, include
from .views import (news_list_view, NewsListView, news_detail_view, sport_news_list_view,

                    NewsUpdateView, NewsDeleteView, NewsCreateView)

urlpatterns = [
    path('', news_list_view, name = 'news_list_page' ),
    path('sport/', sport_news_list_view, name = 'sport_news_page' ),
    # path('all/', NewsListView.as_view(), name = 'news_list_page' ),

    path('<slug>/update/', NewsUpdateView.as_view(), name = 'update_page'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name = 'delete_page'),
    path('news/create/', NewsCreateView.as_view(), name = 'create_page'),


    path('<slug>/', news_detail_view, name = 'news_detail_page' ),
]
