from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from timetable.serializers import GroupSerializer
from timetable.models import Groups


class GroupsList(APIView):
    def get(self, request):
        all_groups = Groups.objects.all()
        serializer = GroupSerializer(all_groups, many=True)

        return Response(serializer.data)
