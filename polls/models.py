from django.db import models
# Create your models here.


class Joke(models.Model):
    category = models.CharField(max_length=255)
    type = models.CharField(max_length=255,default='single')
    setup = models.TextField(null=True)
    delivery = models.TextField(null=True)
    joke = models.TextField(null=False, default="")
    nsfw = models.BooleanField(default=False)
    religious = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    racist = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    explicit = models.BooleanField(default=False)
    safe = models.BooleanField(default=True)
    joke_id = models.IntegerField()
    lang = models.CharField(max_length=2, default="en")

    def __str__(self):
        return self.category