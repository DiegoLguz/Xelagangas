from django.conf.urls import include,url
from django.contrib import admin
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', post_views.post_login, name ="login"),
    url(r'^$', post_views.post_list, name ="list"),
    url(r'^create/', post_views.post_create, name ="crear"),
    url(r'^(?P<id>\d+)/', post_views.post_detail, name ='detail'),
    url(r'^edit/(?P<id>\d+)/', post_views.post_update, name = 'update'),
    url(r'^delete/(?P<id>\d+)/', post_views.post_delete),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
