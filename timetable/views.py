from rest_framework.views import APIView
from rest_framework.response import Response
from timetable.serializers import TimetableSerializer
from timetable.models import Timetable


class TimetableList(APIView):
    def get(self, request):
        all_groups = Timetable.objects.all()
        serializer = TimetableSerializer(all_groups, many=True)

        return Response({'result': serializer.data})
