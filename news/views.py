from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from news.models import WpPosts
from news.serializers import NewsSerializer


class NewsList(APIView):
    @staticmethod
    def get(request):
        all_news = WpPosts.objects.filter(post_type='post', post_status='publish').order_by(
            '-post_date')
        serializer_class = NewsSerializer(all_news, many=True)

        return Response({'result': serializer_class.data})


class NewsDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return WpPosts.objects.get(pk=pk)
        except WpPosts.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        news = self.get_object(pk)
        serializer_class = NewsSerializer(news)

        return Response(serializer_class.data)
