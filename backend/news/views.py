from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import New, Tag
from .serializers import NewsSerializer


class NewsListView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(RetrieveDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer


class NewsbyTagListView(ListAPIView):
    serializer_class = NewsSerializer
    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        tag = get_object_or_404(Tag, name=tag_name)
        news = tag.news.all()
        return news


@api_view(["POST"])
def like_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    news.likes += 1
    news.save()
    return Response({"likes": news.likes}, status=status.HTTP_200_OK)


@api_view(["POST"])
def dislike_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    news.dislikes += 1
    news.save()
    return Response({"dislikes": news.dislikes}, status=status.HTTP_200_OK)


@api_view(["POST"])
def increment_views(request, pk):
    news = get_object_or_404(New, pk=pk)
    news.views += 1
    news.save()
    return Response({"views": news.views}, status=status.HTTP_200_OK)
