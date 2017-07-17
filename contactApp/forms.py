from django import forms

from .models import Contact_form

class AjaxContactForm(forms.ModelForm):

    class Meta:
        model = Contact_form
        fields = ('subject','email','message',)