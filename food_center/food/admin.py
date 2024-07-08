from django.contrib import admin

from .models import FoodType,Composition,Food,Comment

@admin.register(Food)
class FootAdmin(admin.ModelAdmin):
    list_display = ['id','name','food_type','price']
    list_editable = ['price']
    list_filter = ['id','name']
    list_display_links = ['name','id']


admin.site.register(FoodType)
admin.site.register(Composition)
admin.site.register(Comment)
