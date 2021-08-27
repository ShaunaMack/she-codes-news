from django.contrib import admin
from .models import NewsStory

# Register your models here.
class NewsStoryAdmin(admin.ModelAdmin):
    list_filter = ("author",)
    list_display = ("title", "author", "pub_date",)


admin.site.register(NewsStory, NewsStoryAdmin)