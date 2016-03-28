from django.db import models


class Timetable(models.Model):
    timetable_name = models.CharField(max_length=50)
    week_day = models.CharField(choices=(('Monday', 'monday'), ('Tuesday', 'tuesday')))

    def __str__(self):
        return self.timetable_name


class Lesson(models.Model):
    lesson = models.CharField(max_length=50)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)


class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name
