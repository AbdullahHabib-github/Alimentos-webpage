from django.shortcuts import render, redirect
from django.db import connection
from django.views import View
from .forms import Addcityform,Chooserestraunt

import pandas as pd



class Admin(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'appmanager/administrator.html')
    
class Addcity(View):
    def get(self,request,*args,**kwargs):      
        form2 = Addcityform() 
        return render(request, 'appmanager/addcity.html', {'form': form2})
       


    def post(self, request, *args, **kwargs): 

        form2 = Addcityform(request.POST,request.FILES)
        if form2.is_valid():
            C = form2.cleaned_data['City_Name']
            A = form2.cleaned_data['Area_Name']
            F = form2.cleaned_data['Food_Name']
            # FI = form2.cleaned_data['Form_file']
            df = pd.read_excel(request.FILES['Form_file'], names=["name","rating","distance"])
            df.loc[:,'distance']=df.loc[:,'distance'][10:]         
            
            print(df.head())
        
            return redirect('added')
        
           
        # cities  = City.objects.raw("SELECT * FROM customer_city where name = '{}'".format(city_name))
        # areas  = Food_item.objects.raw("SELECT * FROM customer_area where name = '{}'".format(area_name))
        # food  = Food_item.objects.raw("SELECT * FROM customer_area where name = '{}'".format(food_name))
        # # print(cities,type(food_items))

        # if not cities:
        #    with connection.cursor() as cursor:
        #      cursor.execute("INSERT INTO  customer_city (name) VALUES ('{}')".format(city_name))
        #      cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(area_name,city_name))
        # else:
        #    if not areas:
        #        with connection.cursor() as cursor:
        #          cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(area_name,city_name))
        
        # if not food:
        #        with connection.cursor() as cursor:
        #          cursor.execute("INSERT INTO  customer_food_item (name) VALUES ('{}')".format(food_name))


        

class Added(View):
     def get(self,request,*args,**kwargs): 
        return render(request, 'appmanager/added.html')
         
        
class Del(View):
    def get(self,request,*args,**kwargs): 
        form = Chooserestraunt() 
        return render(request, 'appmanager/delete.html', {'form': form})
         
    def post(self,request,*args,**kwargs):
        form = Chooserestraunt(request.POST)
        if form.is_valid():

            data = form.cleaned_data['rest_id']
            request.session['my_data'] = data
            return redirect('deleted')
             

class Deleted(View):
    def get(self,request,*args,**kwargs): 
        return render(request, 'appmanager/deleted.html')
   