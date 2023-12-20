from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('articles/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
