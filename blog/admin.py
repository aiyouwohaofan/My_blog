from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('created_date', 'modified_date', 'author')
    list_display = ('title', 'author', 'created_date', 'modified_date', 'article_views')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
