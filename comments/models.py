from django.db import models

from photos.models import Photo
from users.models import User

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=250)
    date_created = models.DateTimeField()
    photo = models.ForeignKey(Photo)


