from django.contrib import admin

# Register your models here.

# MODELS KO REGISTER KRTE HAI YEHA PR....MIGRATIONS AND MIGRATE KRNE EK BAD...
from . models import  Product, Contact, Orders,OrderUpdate

admin.site.register(Product)

admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)