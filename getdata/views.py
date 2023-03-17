
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

def my_view(request):
    if request.method == 'GET':
        form = MyForm(request.GET)
        if form.is_valid():
            params = {
                'param1': form.cleaned_data['param1'],
                'param2': form.cleaned_data['param2'],
            }
            if form.cleaned_data['checkbox_field']:
                params['checkbox_field'] = ','.join(form.cleaned_data['checkbox_field'])
            url = f'/my_api_endpoint?{params}'
            return HttpResponse(f'<a href="{url}">{url}</a>')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
# Create your views here.
