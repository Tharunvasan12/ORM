# Ex02 Django ORM Web Application
## Date: 26/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-27 184305.png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

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

admin.py

from django.contrib import admin
from .models import loan,loanAdmin
admin.site.register(loan,loanAdmin)
```

## OUTPUT
![alt text](<Screenshot (1).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
