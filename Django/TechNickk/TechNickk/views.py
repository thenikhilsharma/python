#I have created this file
from string import punctuation
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("HI")
    return render(request, 'index.html')

def analyse(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'default')

    print(djtext, removepunc)
    if removepunc == 'on':
        punctuation = '''{}:"<>?_+)(*&^%$#@![];',./-='''
        analysed = ""
        for char in djtext:
            if char not in punctuation:
                analysed += char

        params = {'purpose':'remove Punctutaions', 'analysed_text':analysed}

        #analyse the text
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")

#def capfirst(request):
#    return HttpResponse("capitalise punc")

#def newlineremove(request):
#    return HttpResponse("newline remove")

#def spaceremove(request):
#    return HttpResponse("space remove")

#def charcount(request):
#    return HttpResponse("charcount remove")