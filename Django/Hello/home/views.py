from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "variable1":'this is sent',
        "variable2":'this is sent2'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is HomePage")
def about(request):
    return HttpResponse("This is about Page")
def services(request):
    return HttpResponse("This is services Page")
def contact(request):
    return HttpResponse("This is contact Page")