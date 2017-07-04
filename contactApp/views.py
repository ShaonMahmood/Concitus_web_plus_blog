import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Contact_form

# Create your views here.
#@csrf_exempt
def contact_submit(request):
    if request.method=='POST':
        subject=request.POST['input_name']
        email=request.POST['input_email']
        message=request.POST['input_msg']

        Contact_form.objects.create(
            subject=subject,
            email=email,
            message=message,
            actual_message_time=datetime.datetime.now()
        )
    return HttpResponse('')


def contact_form(request):
    return render(request, 'contactApp/index.html', )