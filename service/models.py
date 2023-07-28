from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()

class SubService(models.Model):
    sub_service_name = models.CharField(max_length=50)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)