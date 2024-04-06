from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from news.forms import CommentForm
from news.models import News, Category


def news_list_view(request):
    all_news = News.published.all()
    latest_post = News.published.all()[:5]
    sport_news_one = News.published.filter(category__name = 'Sport')[0]
    sport_news_all = News.published.filter(category__name = 'Sport')[1:5]
    category = Category.objects.all()

    context = {
        'all_news': all_news,
        'sport_news_one': sport_news_one,
        'sport_news_all': sport_news_all,
        'latest_post': latest_post,
        'category': category
    }
    return render(request, 'news/index.html', context=context)

def sport_news_list_view(request):
    sport_news_one = News.published.filter(category__name = 'Sport')

    context = {
        'sport_news_all': sport_news_one,
    }
    return render(request, 'news/sport_page.html', context=context)







class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'all_news'



def news_detail_view(request, slug):
    news = News.objects.get(slug = slug)

    comments = news.comments.filter(active=True)
    new_comment = None
    comment_count = len(comments)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()



    else:
        comment_form = CommentForm()

    context = {
        "news_detail": news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count,
    }


    return render(request, 'news/single_page.html', context=context)


# def sport_news_list_view(request):
#     all_news = News.published.filter(category__name = 'Sport')
#
#     context = {
#         'sport_news': all_news,
#     }
#
#     return render(request, 'index.html', context=context)



class NewsUpdateView(UpdateView):
    model = News
    fields = ('title','body','category','status', 'image')
    template_name = 'crud/update.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('news_list_page')

class NewsCreateView(CreateView):
    model = News
    fields = ('title','slug', 'body', 'category', 'status', 'image')
    template_name = 'crud/create.html'