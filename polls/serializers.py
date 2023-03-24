from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['category', 'joke','type', 'setup', 'delivery', 'nsfw','religious', 'political', 'racist', 'sexist', 'explicit','joke_id',  'safe', 'lang']