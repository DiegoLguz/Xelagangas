from django.contrib import admin
from posts.models import Post
from posts.models import Archivos
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display= ["title","nombrealbum","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]
    search_fields = ["title","content"]
    class Meta:
        model = Post
        
class ArchivosModelAdmin(admin.ModelAdmin):
    list_display= ["artista","album","updated","timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["artista","album"]
    search_fields = ["artista","album"]
    class Meta:
        model = Archivos
        
admin.site.register(Post,PostModelAdmin)
admin.site.register(Archivos,ArchivosModelAdmin)