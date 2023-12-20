from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_view'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),  # noqa
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),  # noqa
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'),  # noqa
]
