from django.conf.urls import url
from timetable import views

app_name = 'timetable'

urlpatterns = [
    url(r'^$', views.TimetableList.as_view(), name='timetable_list'),
]
