from django.contrib import admin
from .models import Area,Food_item,Restraunt,City

# Register your models here.
admin.site.register(City)

admin.site.register(Area)

admin.site.register(Food_item)

admin.site.register(Restraunt)