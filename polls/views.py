from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question
from .forms import MyForm
import requests

# from .forms import MyForm
def main(request):
    my_name = "Ten toi"
    emotion = ["Smile","Cry","Beep"]
    context ={"name" : my_name, "feeling": emotion}
    return render(request,"polls/index.html", context)
        
def viewList(request):
    list_question = Question.objects.all()
    list = {"quest": list_question}
    return render(request, "polls/question.html",list)




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


