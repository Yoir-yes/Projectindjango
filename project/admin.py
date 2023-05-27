from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tytul','tresc','data_utworzenia','autor','status')
    list_filter = ('autor','data_utworzenia')
    search_fields = ('autor',)
    raw_id_fields = ('autor',)
