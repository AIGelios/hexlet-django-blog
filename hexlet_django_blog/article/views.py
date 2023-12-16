from django.shortcuts import render
from hexlet_django_blog.views import HomepageView
# from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(
        request,
        'articles/articles.html',
        context={'name': __name__}
    )


class ArticlesView(HomepageView):
    template_name = 'articles/articles.html'
