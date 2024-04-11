from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=255, default="#000000")

class Palitra(models.Model):
    name = models.CharField(max_length=255, default="Палитра")
    colors = models.ManyToManyField(Color, blank=True, related_name="palitra")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_colors(self):
        return self.colors.all()