from django import forms
from django.db import connection


class Addrestform(forms.Form):

    City_Name= forms.CharField(label='Enter a City')
    Area_Name= forms.CharField(label='Enter your Area')
    Food_Name= forms.CharField(label='Enter the food Category')
    Form_file = forms.FileField(label='choose a file')


class Chooserestraunt(forms.Form):
        
    with connection.cursor() as cursor:
            cursor.execute("SELECT id , name FROM customer_restraunt")
            rest = cursor.fetchall()
            rest_id= forms.IntegerField(label='Choose a restraunt',  widget=forms.Select(choices=rest))
    
    