from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=400)
    item_pric = models.IntegerField()
    item_image = models.CharField(max_length=1500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0HfIfLCRJFqixc-gE5AW-VvVpSRTGocuTVA&usqp=CAU")
  
    