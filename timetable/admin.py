from django.contrib import admin
from .models import Groups, Lesson, Timetable


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 5


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('group', 'week_day')
    fieldsets = (
        ('Main information', {
            'fields': ('group', 'week_day'),
        }),
        ('Notes', {
            'fields': ('note', ), 'classes': ('collapse',),
        }),
    )
    inlines = [LessonInline]
    list_filter = ['group', 'week_day', ]


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Groups)
