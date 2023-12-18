from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    print("insied form_name_view function")
    
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation successful!")
            
        else:
            print(form.errors)
    else:
        print(request)
        form = forms.FormName()

    return render(request, 'form.html', {'form': form})