from rest_framework import serializers
from .models import Newsmodel
from .models import Tributemodel
from .models import Quotesmodel

class NewsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Newsmodel
        fields = "__all__"

class TributeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Tributemodel
        fields = "__all__"

class QuotesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Quotesmodel
        fields = "__all__"
