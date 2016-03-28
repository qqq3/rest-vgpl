from rest_framework import serializers
from timetable.models import Groups


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('group_name',)
