from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = 'karina | admin'
admin.site.site_title = 'portfolio'
admin.site.index_title = 'karina'

urlpatterns = [
    path('karina_bio/', admin.site.urls),
    path('', views.portfolio),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)