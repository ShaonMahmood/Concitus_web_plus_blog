import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2, GeoIP2Exception
from django.views.decorators.http import require_POST

from .models import Contact_form
from .forms import AjaxContactForm
from ipware.ip import get_real_ip



@require_POST
def contact_submit(request):

    form = AjaxContactForm(request.POST)
    if form.is_valid():

        Contactpost = form.save(commit=False)
        Contactpost.save()

    return HttpResponse('')


def contact_form(request):
    country_code = None
    try:
        ip_addr = get_real_ip(request)
        print("ip_addr: ", ip_addr)
    except Exception as ip_addr_err:
        print('ip_addr_err: {0}'.format(ip_addr_err))
        ip_addr = None

    if ip_addr:
        geo = GeoIP2()
        try:
            country_code = geo.country_code(ip_addr)
        except GeoIP2Exception as geo_err:
            print(geo_err)
    print(country_code)
    return render(request, 'contactApp/index.html',
                  {'country_code_bd': (country_code == 'BD')})
