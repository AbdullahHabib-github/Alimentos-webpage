from django.shortcuts import render
from django.db import connection
from django.views import View
from .models import City,Area,Restraunt,Food_item

# Create your views here.


class Index (View):
    def get(self,request,*args,**kwargs):
        # get every item from each catergory
        #cities = City.objects.all()
        cities  = City.objects.raw("SELECT * FROM customer_city")
 
        context = {
            'cities': cities,
        }
        
        # render the template
        return render(request, 'customer/index.html',context)



    def post(self, request, *args, **kwargs):  
        city_name = request.POST.getlist('city')

        areas  = Area.objects.raw("SELECT * FROM customer_area  where city_id in (select id from customer_city where name = '{}')".format(city_name[0]))

        food_items  = Food_item.objects.raw("SELECT * FROM customer_food_item")


        context = {
        'areas':areas,
        'food_items':food_items,
        }

        return render(request, 'customer/area_dropdown.html', context) 
        

        

        


# class food_area(View):
#     def get(self,request,*args,**kwargs):
#         return render(request, 'customer/area_dropdown.html')
        

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'customer/about.html')
    


class Restruantdisplay(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'customer/restraunt_dis.html')
    


    def post(self,request,*args,**kwargs):
        
        area_name = request.POST.get('area')
        food_name = request.POST.get('food')
        rest = Restraunt.objects.raw("SELECT * FROM customer_restraunt where area_id in (select id from customer_area where name = '{}') and Food_item_id in (select id from customer_Food_item where name = '{}')".format(area_name,food_name))
        context = {
        'rest':rest,
        }
        
        return render(request, 'customer/restraunt_dis.html',context) 



