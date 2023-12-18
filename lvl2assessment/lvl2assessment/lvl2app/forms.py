from django.forms import ModelForm
from . import models



class signUp(ModelForm):
    class Meta:
        model = models.USERS
        fields = '__all__'