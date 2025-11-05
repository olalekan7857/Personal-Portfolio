from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contact_message)
class Contact_messageAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name','phone_number','email','message','date')


admin.site.register(Tools)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('website_name', 'flyer', 'website_url')    