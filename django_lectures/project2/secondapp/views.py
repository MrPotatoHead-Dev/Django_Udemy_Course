from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world. You're at the secondapp index.")

def helperPage(request):
    my_dict = {'insert_me': "Help Help Help !!"}
    return render(request, "secondapp/helper_page.html", context=my_dict)

def mainPage(request):
    return HttpResponse("This is the '/' page where nothing much matters")
def imagePage(request):
        return render(request, "secondapp/image.html")
