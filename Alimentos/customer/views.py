from django.shortcuts import render, redirect
from django.db import connection
from django.views import View
from .models import Restraunt
from appmanager.models import Restricted_Restraunt
from .forms import Choosecity,ChooseAreaFood
from sqlalchemy import create_engine, MetaData, Table, select
import sqlalchemy
from sqlalchemy.orm import Session
        
# Create your views here.
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('mysql://dbuser:main!1234@localhost:3306/testdb')


class Index (View):
 
    
    def get(self,request,*args,**kwargs):

        metadata = MetaData()


        Del_restraunt_table = Table('appmanager_restricted_restraunt', metadata, autoload=True, autoload_with=engine)
        dele = Del_restraunt_table.delete()
        engine.execute(dele)
 

        restraunt_table = Table('customer_restraunt', metadata, autoload=True, autoload_with=engine)
        stmt = select([restraunt_table])
        result = engine.connect().execute(stmt)
        for row in result:
             print(row)



        form = Choosecity()
        return render(request, 'customer/index.html', {'form': form})
        


    def post(self, request, *args, **kwargs):  

        form = Choosecity(request.POST)
        if form.is_valid():

            data = form.cleaned_data['City_id']

            request.session['my_data'] = data
            return redirect('areaandfood')
        
        

class AreaandFood (View):
     
    def get(self,request,*args,**kwargs):

        form_city_id = request.session.get('my_data')
        form = ChooseAreaFood(form_city_id)
        # del request.session['my_data']
        return render(request, 'customer/area_dropdown.html', {'form': form})
        
    def post(self,request,*args,**kwargs):

        
        form = ChooseAreaFood(request.POST)
       
        if form.is_valid():

            data = form.cleaned_data['Area_id']
            data2 = form.cleaned_data['Food_id']
        
            request.session['my_data2'] = data
            request.session['my_data3'] = data2
            return redirect('restraunt')



       

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'customer/about.html')
    


class Restruantdisplay(View):

    def get(self,request,*args,**kwargs):

        form_area_id = request.session.get('my_data2')
        form_food_id = request.session.get('my_data3')
        del request.session['my_data2']
        del request.session['my_data3']

        rest = Restraunt.objects.raw("SELECT * FROM customer_restraunt where (Area_id = {} and Food_item_id = {})".format(form_area_id,form_food_id))
        context = {
        'rest':rest,
        }
        
        return render(request, 'customer/restraunt_dis.html',context) 

    