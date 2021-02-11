from django.contrib import admin
from django.urls import path, re_path,include
from django.conf.urls import url
from django.views.generic import TemplateView
from ngo2.views import index
from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('ngo2.urls')),
    re_path('', TemplateView.as_view(template_name="index.html"))
] 


