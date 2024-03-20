from django.contrib import admin

from .models import Category, News
# Register your models here.


@admin.register(News)
class AdminSite(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category', 'publish_time', 'status']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','body']


admin.site.register(Category)