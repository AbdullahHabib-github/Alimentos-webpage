from django.db import models
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('mysql://dbuser:main!1234@localhost:3306/testdb')
Base = declarative_base()




class Admin_user(Base):
    __tablename__ = 'admin_user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    


class Area(models.Model):
    City =models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Food_item (models.Model):
    name = models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.name
    


class Restraunt (models.Model):
    Area =models.ForeignKey(Area, on_delete=models.CASCADE)
    Food_item = models.ForeignKey(Food_item, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=200)
    rating = models.FloatField()
    
    
    def __str__(self):
        return self.name
    
 