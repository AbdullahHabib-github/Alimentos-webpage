from django.db import models
from customer.models import Area,Food_item
# Create your models here.

class Restricted_Restraunt (models.Model):
    Area =models.ForeignKey(Area, on_delete=models.CASCADE)
    Food_item = models.ForeignKey(Food_item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=200)
    rating = models.IntegerField()
    
    
    def __str__(self):
        return self.name   