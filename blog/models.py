from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=255)
    complete = models.BooleanField(default=True)

    def __str__(self):
        return self.text


