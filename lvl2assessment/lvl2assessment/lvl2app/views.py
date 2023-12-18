from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lvl2app.models import USERS
from .forms import signUp
# Create your views here.
def index(request):
    return render(request, 'welcomePage/welcomePage.html')

def users(request):
    users_lst = USERS.objects.order_by('last_name')
    user_dict = {'user_details': users_lst}
    return render(request, 'users/users.html', context=user_dict)

def sign_up_user(request):
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            
            new_user = form.save()
            print(new_user)
            return HttpResponseRedirect('/')
        else:
            raise Exception("The form data was invalid")
    else:
        form = signUp()
    
    return render(request, 'createuser/signup.html', {'form':form})