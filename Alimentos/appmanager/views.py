from django.shortcuts import render
from django.db import connection
from django.views import View
from customer.models import City,Food_item
import pandas as pd
# Create your views here.


class Admin(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'appmanager/administrator.html')


class Addcity(View):
    def get(self,request,*args,**kwargs):       
        return render(request, 'appmanager/addcity.html')
   

    def post(self, request, *args, **kwargs):  
        city_name = request.POST.get('CityName')
        area_name= request.POST.get('AreaName')
        food_name= request.POST.get('FoodName')
        file_name= request.POST.get('FileName')
        
        cities  = City.objects.raw("SELECT * FROM customer_city where name = '{}'".format(city_name))
        areas  = Food_item.objects.raw("SELECT * FROM customer_area where name = '{}'".format(area_name))
        food  = Food_item.objects.raw("SELECT * FROM customer_area where name = '{}'".format(food_name))
        # print(cities,type(food_items))

        if not cities:
           with connection.cursor() as cursor:
             cursor.execute("INSERT INTO  customer_city (name) VALUES ('{}')".format(city_name))
             cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(area_name,city_name))
        else:
           if not areas:
               with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(area_name,city_name))
        
        if not food:
               with connection.cursor() as cursor:
                 cursor.execute("INSERT INTO  customer_food_item (name) VALUES ('{}')".format(food_name))


        df = pd.read_excel( "\\customer\\"+file_name,names=["name","rating","distance"])

        print(df)
        # for i in range(0,df.shape[0]):
        #    df.loc[i,'distance']=df.loc[i,'distance'][10:]         
       

       
        context = {
        # 'areas':cities,
        # 'food_items':food_items,
         }

        return render(request, 'appmanager/addcity.html', context) 
        
class Junk(View):
    def get(self,request,*args,**kwargs): 
        return render(request, 'appmanager/junk.html')
         