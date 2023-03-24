from django.db import models
# Create your models here.

class Question (models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
class Choice (models.Model):
    question  = models.ForeignKey(Question,on_delete=models.CASCADE )
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

class Joke(models.Model):
    category = models.CharField(max_length=255)
    # type = models.CharField(max_length=255)
    # setup = models.TextField(null=True)
    # delivery = models.TextField(null=True)
    joke = models.TextField(null=False, default="")
    # nsfw = models.BooleanField(default=False)
    # religious = models.BooleanField(default=False)
    # political = models.BooleanField(default=False)
    # racist = models.BooleanField(default=False)
    # sexist = models.BooleanField(default=False)
    # explicit = models.BooleanField(default=False)
    # safe = models.BooleanField(default=True)
    # joke_id = models.IntegerField(unique=True)
    # lang = models.CharField(max_length=2, default="en")

    def __str__(self):
        return self.category