from django.contrib import admin
from .models import Site, Item, BusinessProcess, FileUpload

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
    list_filter = ('site',)

@admin.register(BusinessProcess)
class BusinessProcessAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('site', 'item', 'process', 'uploaded_at')
    list_filter = ('site', 'item', 'process')
