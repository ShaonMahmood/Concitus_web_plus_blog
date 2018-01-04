#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function, unicode_literals
import os
import time
import json

import sys

import set_env

import datetime


DEBUG = True

#logger = set_env.get_logger(debug=DEBUG)









#exclude_condition = ['trying', 'failed', 'no-answer', 'busy']


#json_decoder = json.JSONDecoder()


def main():

    fromaddr = "mahmood.shaon@concitus.com"
    toaddr = "mahmood.shaon@concitus.com"
    for obj in Contact_form.objects.filter(message_delivered=False).order_by('actual_message_time')[:3]:
        #logger.info("lead_info: {0}".format(obj.subject))
        try:
            email = EmailMessage(
                obj.subject,
                obj.message,
                fromaddr,
                [toaddr],
                ['bcc@example.com'],
                reply_to=[obj.email],
                )

            email.send()
            obj.message_delivered = True
            obj.message_delivary_time = datetime.datetime.now()
            obj.save(update_fields=['message_delivered','message_delivary_time'])
                    #server.quit()

        except Exception as err:
            print("Sending Error", err)
                    #server.quit()


    

if __name__ == '__main__':
    set_env.activate_venv()



    from django.core.mail import EmailMessage
    from contactApp.models import Contact_form
    while True:
        main()
        time.sleep(2)


        