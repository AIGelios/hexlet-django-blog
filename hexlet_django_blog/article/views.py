from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article

# from django.http import HttpResponse
# Create your views here.


def article(request, tags, article_id):
    return render(
        request,
        'articles/articles.html',
        context={'body': f'Статья номер {article_id}. Тег {tags}'}
    )


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={'article': article}
        )
