from rest_framework import serializers
from news.models import WpPosts


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        models = WpPosts
        fields = ('id', 'post_title', 'post_content', 'post_date')
