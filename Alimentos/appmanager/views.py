from django.shortcuts import render, redirect
from django.db import connection
from django.views import View
from .forms import Addrestform,Chooserestraunt
from customer.models import Area,Food_item,City
import pandas as pd



class Admin(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'appmanager/administrator.html')
    
class Addrest(View):
    def get(self,request,*args,**kwargs):      
        form2 = Addrestform() 
        return render(request, 'appmanager/addrest.html', {'form': form2})
       


    def post(self, request, *args, **kwargs): 

        form2 = Addrestform(request.POST,request.FILES)
        if form2.is_valid():
            C = form2.cleaned_data['City_Name']
            A = form2.cleaned_data['Area_Name']
            F = form2.cleaned_data['Food_Name']

            cities  = City.objects.raw("SELECT * FROM customer_city where name = '{}'".format(C))
            areas  = Area.objects.raw("SELECT * FROM customer_area where name = '{}'".format(A))
            food  = Food_item.objects.raw("SELECT * FROM customer_food_item where name = '{}'".format(F))
            # print(cities,type(food_items))
            # print(C,A,F)
      
            if not cities:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO  customer_city (name) VALUES ('{}')".format(C))
                    cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(A,C))
            else:
                if not areas:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',(select id from customer_city where name = '{}' ))".format(A,C))

                        # cursor.execute("INSERT INTO  customer_area (name,city_id) VALUES ('{}',{})".format(A,1))
                    
            if not food:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO  customer_food_item (name) VALUES ('{}')".format(F))

            with connection.cursor() as cursor:
                cursor.execute("SELECT id FROM customer_area where (name = '{}' and City_id in (select id from customer_city where name ='{}'))".format(A,C))
                # cursor.execute("SELECT id FROM customer_area where (name = '{}' and City_id = {})".format(A,1))
                Ar = cursor.fetchall()
                cursor.execute("SELECT id FROM customer_food_item where name = '{}'".format(F))
                Fr = cursor.fetchall()
                     
            # print(," ",Ar[0][0])
            # FI = form2.cleaned_data['Form_file']
            df = pd.read_excel(request.FILES['Form_file'], names=["name","rating","address"])
            df.address = df.address.str.split(" · ").str[1]
            mask = df.address.str.contains("P3")
            df = df[~mask]
            df.dropna(how="any",inplace=True) 
            # with connection.cursor() as cursor:
            #    cursor.execute("Insert into customer_restraunt  values (id  ={})".format(data))
            
            for index, row in df.iterrows():
                  with connection.cursor() as cursor:
                     cursor.execute("INSERT INTO customer_restraunt (name, address, rating, Food_item_id,Area_id) values('{}','{}',{},{},{})".format(row["name"], row["address"],row["rating"],Fr[0][0],Ar[0][0]))
            
            return redirect('added')
        
           
        

        

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
            with connection.cursor() as cursor:
               cursor.execute("Delete from customer_restraunt  where (id  ='{}')".format(data))
            request.session['my_data'] = data
            return redirect('deleted')
             

class Deleted(View):
    def get(self,request,*args,**kwargs): 
        return render(request, 'appmanager/deleted.html')
    
    def post(self,request,*args,**kwargs):
        with connection.cursor() as cursor:
            cursor.execute("CALL copy_restricted_to_customer()")
            cursor.execute("Delete from appmanger_restricted_restraunt")
             
        return redirect('D')
             
class D(View):
    def get(self,request,*args,**kwargs): 
            return render(request, 'appmanager/D.html')
    