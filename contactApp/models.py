from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Contact_form(models.Model):
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    actual_message_time=models.DateTimeField(auto_now=True)
    message_delivered=models.BooleanField(default=False)
    message_delivary_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.subject+" "+self.email+" "+str(self.message_delivered)

