from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerialize
from .serializers import QuotesSerialize
from .serializers import TributeSerialize
from .models import Newsmodel
from .models import Tributemodel
from .models import Quotesmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
# Create your views here.

index = never_cache(TemplateView.as_view(template_name="index.html"))
    

@api_view(['GET'])
def shownewsmodels(request):
    newsobj=Newsmodel.objects.all()
    
    NewsSerializeobj=NewsSerialize(newsobj,many=True)
    
    Resultmodel= NewsSerializeobj.data
    return Response(Resultmodel)



@api_view(['GET'])
def showtributemodels(request):
   
    tributeobj=Tributemodel.objects.all()
    
    
    TributeSerializeobj=TributeSerialize(tributeobj,many=True)
   
    Resultmodel=  TributeSerializeobj.data 
    return Response(Resultmodel)



@api_view(['GET'])
def showquotesmodels(request):
   

    quotesobj=Quotesmodel.objects.all()
    

    QuotesSerializeobj=QuotesSerialize(quotesobj,many=True)
    Resultmodel=  QuotesSerializeobj.data
    return Response(Resultmodel)