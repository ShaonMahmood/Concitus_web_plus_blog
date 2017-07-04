import click
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime,time

from django.core.mail import EmailMessage

from contactApp.models import Contact_form
#@click.command()
#def cli():
    #"""Example script."""
    #click.echo('Hello World!')

"""@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)"""



@click.command()
def cli():
    fromaddr = "mahmood.shaon@concitus.com"
    toaddr = "concitus@concitus.com"
    while True:
        try:
            for obj in Contact_form.objects.filter(message_delivered=False).order_by('actual_message_time')[:3]:

                try:
                    email = EmailMessage(
                        obj.subject,
                        obj.message,
                        fromaddr,
                        [toaddr],
                        ['bcc@example.com'],
                        reply_to=[obj.email],
                        headers={'Message-ID': 'foo'},
                    )

                    email.send()
                    obj.message_delivered = True
                    obj.message_delivary_time = datetime.datetime.now()
                    obj.save()
                    # server.quit()

                except:
                    print("Sending Error")
                    # server.quit()


        except:
            print("No objects")


        time.sleep(3)





