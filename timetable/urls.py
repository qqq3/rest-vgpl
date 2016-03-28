from django.conf.urls import url
from timetable import views

app_name = 'timetable'

urlpatterns = [
    url(r'^$/', views.GroupsList.as_view(), name='groups_list'),
]
