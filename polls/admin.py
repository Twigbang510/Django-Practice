from django.contrib import admin
from .models import Choice,Question, Joke

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.

class JokeAdmin(admin.ModelAdmin):
    joke_display = ('category')

admin.site.register(Joke,JokeAdmin)