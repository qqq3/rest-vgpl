from rest_framework import viewsets

from news.models import WpPosts
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = WpPosts.objects.filter(post_type='post', post_status='publish').order_by(
        '-post_date')
    serializer_class = NewsSerializer
