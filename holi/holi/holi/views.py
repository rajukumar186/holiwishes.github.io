from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'holi.html')
def new(request):
    dj_text = request.GET.get('text')
    print(dj_text)
    analyzed = dj_text.title()

    params = {"analyzed_text": analyzed}
    return render(request, 'new.html', params)