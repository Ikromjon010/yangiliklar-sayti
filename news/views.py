from django.shortcuts import render
from django.views.generic import ListView

from news.models import News, Category


def news_list_view(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news,
    }

    return render(request, 'home.html', context=context)


class NewsListView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'all_news'



def news_detail_view(request, id):
    detail = News.objects.get(id = id)

    context = {
        'news_detail': detail,
    }

    return render(request, 'detail.html', context=context)
