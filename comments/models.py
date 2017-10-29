from django.db import models

# Create your models here.


class Comment(models.Model):
    name_user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    comment = models.TextField()

