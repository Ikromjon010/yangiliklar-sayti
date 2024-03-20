from django.shortcuts import render
from django.views.generic import ListView

from news.models import News, Category


def news_list_view(request):
    all_news = News.published.all()
    sport_news_one = News.published.filter(category__name = 'Sport')[0]
    sport_news_all = News.published.filter(category__name = 'Sport')[1:5]

    context = {
        'all_news': all_news,
        'sport_news_one': sport_news_one,
        'sport_news_all': sport_news_all,
    }

    return render(request, 'index.html', context=context)


class NewsListView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'all_news'



def news_detail_view(request, id):
    detail = News.objects.get(id = id)

    context = {
        'news_detail': detail,
    }

    return render(request, 'detail.html', context=context)


# def sport_news_list_view(request):
#     all_news = News.published.filter(category__name = 'Sport')
#
#     context = {
#         'sport_news': all_news,
#     }
#
#     return render(request, 'index.html', context=context)
