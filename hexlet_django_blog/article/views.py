from django.shortcuts import render, redirect
from hexlet_django_blog.views import HomepageView
# from django.http import HttpResponse
# Create your views here.


def article(request, tags, article_id):
    return render(
        request,
        'articles/articles.html',
        context={'body': f'Статья номер {article_id}. Тег {tags}'}
    )


class ArticlesView(HomepageView):
    template_name = 'articles/articles.html'
