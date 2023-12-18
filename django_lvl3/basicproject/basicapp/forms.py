from django import forms
from django.core import validators

#Custom validation functions
def check_first_letter(value):
    if value[0].lower() != 'j':
        raise forms.ValidationError("The first letter does not start with 'j' !")


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_first_letter])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Re-enter your email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    #cleans out the enture form
    def clean(self):
        all_clean = super().clean()
        print(all_clean)
        email = all_clean['email']
        vmail = all_clean['verify_email']
        if email != vmail:
            raise forms.ValidationError("The emails you have entered do not match")
    #cleans out a specific input
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
    