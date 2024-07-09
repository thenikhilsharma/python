#I have created this file
from string import punctuation
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def search_profile(request):
    #get the text
    search_text = request.GET.get('search_text', 'default')
    #removepunc = request.GET.get('removepunc', 'default')
    print(search_text)
    if search_text[0] == "@":
        
        username = search_text
        params = {'bio':'18 Y.O', 'username':username}

        return render(request, 'search_profile.html', params)
    else:
        return HttpResponse("Error")

def profile(request):
    return render(request, 'profile.html')

#def newlineremove(request):
#    return HttpResponse("newline remove")

#def spaceremove(request):
#    return HttpResponse("space remove")

#def charcount(request):
#    return HttpResponse("charcount remove")