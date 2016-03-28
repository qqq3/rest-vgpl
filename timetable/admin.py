from django.contrib import admin
from .models import Groups, Lesson, Timetable


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('timetable_name', 'group', )
    inlines = [LessonInline]


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Groups)
