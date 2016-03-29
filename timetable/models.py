from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name


class Timetable(models.Model):
    timetable_name = models.CharField(max_length=50)
    week_day = models.CharField(max_length=30,
                                choices=(('Monday', 'monday'), ('Tuesday', 'tuesday')))
    group = models.ForeignKey(Groups)

    def __str__(self):
        return self.timetable_name


class Lesson(models.Model):
    lesson = models.CharField(max_length=50)
    timetable = models.ForeignKey(Timetable, related_name='lessons')

    def __str__(self):
        return self.lesson

