from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100, default='None')
    mobileNumber = models.CharField(max_length=10, default=0)
    gamesWon = models.IntegerField(default=0)
    gamesLost = models.IntegerField(default=0)
    gamesDrawn = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)
