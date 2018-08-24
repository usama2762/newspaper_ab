from django.db import models

# Create your models here.
class RequestStore(models.Model):
    request_time = models.DateTimeField(null=True)
    request_url = models.CharField(max_length=100,default=None)
    request_method = models.CharField(max_length=20,default=None,null=True,blank=True)
    status_code = models.IntegerField(default=200,null=True,blank=True)
