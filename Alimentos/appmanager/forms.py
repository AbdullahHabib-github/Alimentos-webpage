from django import forms
from django.db import connection


class Addcityform(forms.Form):

    City_Name= forms.CharField(label='Enter a City')
    Area_Name= forms.CharField(label='Enter your Area')
    Food_Name= forms.CharField(label='Enter the food that you want to eat')
    Form_file = forms.FileField(label='choose a file')


class Chooserestraunt(forms.Form):
        
    with connection.cursor() as cursor:
            # cursor.execute("SELECT id , name FROM customer_area where (City_id = {})".format(city))
            # cursor.execute("SELECT id , name FROM customer_area")
            # areas = cursor.fetchall()
            # cursor.execute("SELECT id , name FROM customer_food_item")
            # food = cursor.fetchall()
            cursor.execute("SELECT id , name FROM customer_restraunt")
            rest = cursor.fetchall()
            
    # Area_id = forms.IntegerField(label='Choose your Area',  widget= forms.Select(choices=areas)) 
    # Food_id= forms.IntegerField(label='Choose your Food',  widget=forms.Select(choices=food))
    rest_id= forms.IntegerField(label='Choose your Food',  widget=forms.Select(choices=rest))
    