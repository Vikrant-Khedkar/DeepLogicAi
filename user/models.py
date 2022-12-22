from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pdf(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf')

    class Meta:
        get_latest_by = ['id']


    def __str__(self):
        return self.pdf.url
        

