from django.contrib import admin
from .models import Profile, Project, Reviewrating
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['profile']
    ordering = ['profile']
    search_fields = ['foreignkeyfield__name']

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register( Reviewrating)
