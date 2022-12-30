from django import forms

from django.db import connection
# from customer.models import Area,City

class Choosecity(forms.Form):

    with connection.cursor() as cursor:
        cursor.execute("SELECT id , name FROM customer_city")
        cities = cursor.fetchall()
   
    City_id= forms.IntegerField(label='Choose your City', widget=forms.Select(choices=cities))


class ChooseAreaFood(forms.Form):
    
    city = 2
    global areas
    global food


    def __init__(self,received_city, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        with connection.cursor() as cursor:
                cursor.execute("SELECT id , name FROM customer_area where (City_id = {})".format(received_city))
                areas = cursor.fetchall()
        # self.Area_id = forms.IntegerField(label='Choose your Area', widget=forms.Select(choices=areas))
        
            # cursor.execute("SELECT id , name FROM customer_food_item")
        with connection.cursor() as cursor:
            cursor.execute("SELECT id , name FROM customer_food_item")
            food = cursor.fetchall()
        # self.Food_id= forms.IntegerField(label='Choose your Food', widget=forms.Select(choices=food))
   

    areas=()
    food=()
    # with connection.cursor() as cursor:
    #         # cursor.execute("SELECT id , name FROM customer_area where (City_id = {})".format(city))
    #         cursor.execute("SELECT id , name FROM customer_area")
    #         areas = cursor.fetchall()
    #         cursor.execute("SELECT id , name FROM customer_food_item")
    #         food = cursor.fetchall()

    Area_id = forms.IntegerField(label='Choose your Area', widget=forms.Select(choices=areas)) 
    Food_id= forms.IntegerField(label='Choose your Food', widget=forms.Select(choices=food))
    