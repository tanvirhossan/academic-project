from django.contrib import admin
from .models import alllist
# Register your models here.

class alllist_Admin(admin.ModelAdmin):
	list_display = ['uname','pimage','placediscription','placeway','imagefigname','shortdiscription']
	
	class Meta:
		model = alllist

admin.site.register(alllist, alllist_Admin)