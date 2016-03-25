from django.conf.urls import url

from news import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.NewsList.as_view(), name='news_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='news_detail'),
]
