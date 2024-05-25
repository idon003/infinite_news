from django.urls import path
from .views import NewsListView, NewsDetailView, NewsbyTagListView, like_news, dislike_news, increment_views

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/tag/<str:tag_name>/', NewsbyTagListView.as_view(), name='news_by_tag'),
    path('news/<int:pk>/like/', like_news, name='like_news'),
    path('news/<int:pk>/dislike/', dislike_news, name='dislike_news'),
    path('news/<int:pk>/increment-views/', increment_views, name='increment_views'),
]
