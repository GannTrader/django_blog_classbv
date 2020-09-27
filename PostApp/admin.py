from django.contrib import admin
from PostApp.models import Posts, Catagory

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'catagory', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title', 'body']

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title', 'body']

admin.site.register(Posts, PostAdmin)
admin.site.register(Catagory, CatagoryAdmin)