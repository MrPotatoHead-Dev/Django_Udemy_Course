from django.shortcuts import render
from django.http import HttpResponse
from projectapps.models import *
# Create your views here.
def index(request):
    return HttpResponse("Welcome to the app index from projectapps/views.py")

def helperPage(request):
    
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpage_list}
    return render(request, 'helper_page.html', context=date_dict)

def entrySignal(request):
    return render(request, 'trading_page.html')

def mtv(request):

    return render(request, )