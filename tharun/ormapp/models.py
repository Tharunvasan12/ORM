from django.db import models
from django.contrib import admin
class loan(models.Model):
    Name=models.CharField(max_length=20)
    Acc_no=models.IntegerField(primary_key=True)
    Dob=models.DateField()
    Email=models.EmailField()
    Balance=models.FloatField(default=0)
class loanAdmin(admin.ModelAdmin):
    list_display=('Name','Acc_no','Dob','Email','Balance')