from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import MyForm
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from polls.models import Joke
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
# from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            category = [str(x) for x in request.POST.getlist('category_choice')]
            flags = [str(y) for y in request.POST.getlist('flags_choice')]
            types = [str(z) for z in request.POST.getlist('types_choice')]
            keyword_url = ''.join((request.POST.getlist('keyword')))
            start_amount = ''.join(request.POST.getlist('start'))
            end_amount = ''.join(request.POST.getlist('end'))
            id_url = f"{start_amount}-{end_amount}"
            amount = ''.join(request.POST.getlist('amount'))
            category_url = ','.join(category)
            flags_url = ','.join(flags)
            types_url = ','.join(types)
            lang_url = ','.join(request.POST.getlist('lang_select'))
            main_url =  f"https://v2.jokeapi.dev/joke/{category_url}?lang={lang_url}&blacklistFlags={flags_url}&contains={keyword_url}&idRange={id_url}&amount={amount}"
            if len(types) == 1:
                main_url =  f"https://v2.jokeapi.dev/joke/{category_url}?lang={lang_url}&blacklistFlags={flags_url}&type={types_url}&contains={keyword_url}&idRange={id_url}&amount={amount}"
            url = requests.get(main_url)
            if url.status_code == 200:
                data = url.json()
            return render(request, 'polls/result.html', {'category': category, 'main_url' : main_url, 'data' : data, 'flags' : flags, 'types' : types, 'keyword' : keyword_url, 'id': id_url, 'amount': amount, 'lang' : lang_url})
    else:
        form = MyForm()
    context = {'form': form}
    return render(request, 'polls/form.html', context)

@api_view(['GET'])
def joke_list_get(request,  category):
    if request.method == 'GET':
        data = Joke.objects.filter(category= category) 

        serializer = JokeSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
        

@api_view(['POST'])
def joke_list_post(request):
    if request.method == 'POST':
        serializer = JokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
