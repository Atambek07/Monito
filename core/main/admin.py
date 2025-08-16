from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Costumer)
admin.site.register(models.Pets)
admin.site.register(models.Product)
admin.site.register(models.PetKnowledge)
admin.site.register(models.ProductDetail)
admin.site.register(models.Seller)