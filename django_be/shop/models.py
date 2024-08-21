from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_absolute_url(self):
        #return f"/product/lookup/{self.id}"
        return reverse("shop:lookup", kwargs = { "my_id" : self.id })