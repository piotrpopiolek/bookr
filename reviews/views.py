from django.shortcuts import render

def index(request):
    return render(request,'base.html')

def search(request):
    phrase = request.GET.get('phrase') or ''
    return render(request,'resultSearch.html',{"phrase":phrase})