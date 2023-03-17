from django.db import models
# Create your models here.

class Question (models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
class Choice (models.Model):
    question  = models.ForeignKey(Question,on_delete=models.CASCADE )
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

class Flags(models.Model):
    nsfw = models.BooleanField()
    religious = models.BooleanField()
    political = models.BooleanField()
    racist = models.BooleanField()
    sexist = models.BooleanField()
    explicit = models.BooleanField()
class Joke(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    setup = models.CharField(max_length=500)
    delivery = models.CharField(max_length=500)
    flags = models.ForeignKey(Flags, on_delete=models.CASCADE)
    safe = models.BooleanField()
    joke_id = models.IntegerField()