from django.contrib import admin
from .models import News, MenuItem, Teacher
from mptt.admin import MPTTModelAdmin

admin.site.register(News)
admin.site.register(Teacher)
 
class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)

