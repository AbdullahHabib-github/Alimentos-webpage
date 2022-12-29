from django.db import models

# Create your models here.



class City(models.Model):
    name = models.CharField(max_length=30)
    #image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return self.name
    


class Area(models.Model):
    City =models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Food_item (models.Model):
    name = models.CharField(max_length=40)
    #image = models.ImageField(upload_to='food_images/')
    
    
    def __str__(self):
        return self.name
    


class Restraunt (models.Model):
    Area =models.ForeignKey(Area, on_delete=models.CASCADE)
    Food_item = models.ForeignKey(Food_item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=200)
    rating = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
 