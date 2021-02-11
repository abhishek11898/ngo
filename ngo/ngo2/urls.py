from django.urls import path
from . import views
from django.urls import re_path,include
from django.conf.urls import url
from django.views.generic import TemplateView
from ngo2.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
  path('model/news/', views.shownewsmodels),
  path('model/tribute/', views.showtributemodels),
  path('model/quotes/', views.showquotesmodels),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)