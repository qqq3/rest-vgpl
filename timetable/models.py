from django.db import models


class Groups(models.Model):
    group_name = models.IntegerField(max_length=25)

