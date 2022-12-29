from django import forms

from django.db import connection
# from customer.models import Area,City

class Choosecity(forms.Form):

    with connection.cursor() as cursor:
        cursor.execute("SELECT id , name FROM customer_city")
        cities = cursor.fetchall()
   
    City_id= forms.IntegerField(label='Choose your City', widget=forms.Select(choices=cities))


class ChooseAreaFood(forms.Form):
    
    city = 1


    # def __init__(self,received_city, *args, **kwargs):
    #     super().__init__(*args, **kwargs) 
    #     print("You are calling me")
    #     print("old",self.city)
    #     self.city = received_city
    #     with connection.cursor() as cursor:
    #             cursor.execute("SELECT id , name FROM customer_area where (City_id = {})".format(self.city))
    #             areas = cursor.fetchall()
    #     self.Area_id = forms.IntegerField(label='Choose your Area', widget=forms.Select(choices=areas))
        
    #         # cursor.execute("SELECT id , name FROM customer_food_item")
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT id , name FROM customer_food_item")
    #         food = cursor.fetchall()
    #     self.Food_id= forms.IntegerField(label='Choose your Food', widget=forms.Select(choices=food))
   

    
    with connection.cursor() as cursor:
            # cursor.execute("SELECT id , name FROM customer_area where (City_id = {})".format(city))
            cursor.execute("SELECT id , name FROM customer_area")
            areas = cursor.fetchall()
            cursor.execute("SELECT id , name FROM customer_food_item")
            food = cursor.fetchall()
    Area_id = forms.IntegerField(label='Choose your Area', widget=forms.Select(choices=areas)) 
    Food_id= forms.IntegerField(label='Choose your Food', widget=forms.Select(choices=food))
    


# from dynamic_forms.forms import DynamicForm

# def formfield_callback(field):
#     if field.name == 'country':
#         return ('country', forms.ChoiceField(choices=COUNTRY_CHOICES))
#     elif field.name == 'area':
#         return ('area', forms.ChoiceField(choices=AREA_CHOICES))
#     return field.name, field

# class MyForm(DynamicForm):
#     formfield_callback = formfield_callback

