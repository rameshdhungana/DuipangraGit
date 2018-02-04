from django.contrib import admin
from django.contrib.auth.models import User
from .models import Bikeobject,all_and_user,Place,Restuarent,Specialuser,Supplier,Blog,Author,Entry,Customer
# Register your models here.
admin.site.register(Bikeobject)
admin.site.register(all_and_user)
admin.site.register(Place)
admin.site.register(Specialuser)
admin.site.register(Supplier)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Customer)
