from django.contrib import admin
from .models import Post,AboutUs

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title','content')

admin.site.register(Post,PostAdmin)
admin.site.register(AboutUs)
