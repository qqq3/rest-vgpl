from rest_framework import serializers
from news.models import WpPosts


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='post_title')
    content = serializers.CharField(source='post_content')
    date = serializers.DateTimeField(source='post_date')

    class Meta:
        model = WpPosts
        fields = ('id', 'title', 'content', 'date')
