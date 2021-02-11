from django.contrib import admin
from .models import Newsmodel
from .models import Tributemodel
from .models import Quotesmodel


# Register your models here.
admin.site.register(Newsmodel)
admin.site.register(Tributemodel)
admin.site.register(Quotesmodel)