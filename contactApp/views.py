import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST

from .models import Contact_form
from .forms import AjaxContactForm
# Create your views here.
@require_POST
def contact_submit(request):

    form = AjaxContactForm(request.POST)
    if form.is_valid():

        Contactpost = form.save(commit=False)
        Contactpost.save()

    return HttpResponse('')



def contact_form(request):
    return render(request, 'contactApp/index.html', )