from django.conf.urls import url

from news.views import NewsViewSet

app_name = 'news'

news_list = NewsViewSet.as_view({
    'get': 'list',
})
news_detail = NewsViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    url(r'^$', news_list, name='news_list'),
    url(r'^(?P<pk>[0-9]+)/$', news_detail, name='news_detail'),
]
