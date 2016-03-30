from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name

    class Meta:
        managed = True
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Timetable(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    timetable_name = models.CharField(max_length=50)
    week_day = models.CharField(max_length=30, choices=DAY_CHOICES)
    group = models.ForeignKey(Groups)

    def __str__(self):
        return self.timetable_name

    class Meta:
        managed = True
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetables'


class Lesson(models.Model):
    lesson = models.CharField(max_length=50)
    timetable = models.ForeignKey(Timetable, related_name='lessons')

    def __str__(self):
        return self.lesson
