from django.shortcuts import render, redirect
from django.db import connection
from django.views import View
from .models import Restraunt
from .forms import Choosecity,ChooseAreaFood


# Create your views here.


class Index (View):
 
    
    def get(self,request,*args,**kwargs):
        
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

        # form_city_id = request.session.get('my_data')
        form = ChooseAreaFood()#form_city_id)
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


   