from rest_framework.filters import DjangoFilterBackend
from rest_framework import generics
from timetable.serializers import TimetableSerializer
from timetable.models import Timetable


class TimetableList(generics.ListAPIView):
    serializer_class = TimetableSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('week_day',)

    def get_queryset(self):
        queryset = Timetable.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group__group_name=group)
        return queryset
