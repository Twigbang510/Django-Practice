from django.contrib import admin
from .models import  Joke


# Register your models here.

class JokeAdmin(admin.ModelAdmin):
    joke_display = ('category')

admin.site.register(Joke,JokeAdmin)