from django.db import models
from users.models import User

# Create your models here.

class Photo(models.Model):

    path = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


