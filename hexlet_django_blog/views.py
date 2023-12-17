# hexlet_django_blog/views.py
from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.views import View
from django.views.generic.base import TemplateView
from django.urls import reverse


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def homepage(request):
    return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')
