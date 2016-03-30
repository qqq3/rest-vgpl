from rest_framework import serializers
from timetable.models import Groups, Timetable


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('group_name',)


class TimetableSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    lessons = serializers.SlugRelatedField(many=True, read_only=True,
                                           slug_field='lesson')

    class Meta:
        model = Timetable
        fields = ('group', 'week_day', 'lessons',)
