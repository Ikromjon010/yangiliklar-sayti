from django.contrib import admin

from .models import Category, News, Comment


# Register your models here.


@admin.register(News)
class AdminSite(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category', 'publish_time', 'status']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','body']


admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'news', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    # search_fields = ['body', 'user']
    actions = ['disable_comment', 'enable_comment']

    def disable_comment(self, request, queryset):
        queryset.update(active = False)


    def enable_comment(self, request, queryset):
        queryset.update(active = True)
