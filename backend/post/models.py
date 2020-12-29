from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Bachelor_data(models.Model):
    number = models.IntegerField(max_length=4)
    data = models.TextField()

    def __str__(self):
        return str(self.number)
