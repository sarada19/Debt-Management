from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.db.models import F,Sum

class User_objects(generics.ListAPIView):
    queryset = USer_Model.objects.all()
    sum_owes = USer_Model.objects.aggregate(Sum('owes__amount'))
    sum_owed_by  = USer_Model.objects.aggregate(Sum('owed_by__amount'))
    for i in sum_owes.values():
        i
    for j in sum_owed_by.values():
        j
    total = i- j
    query = USer_Model.objects.update(**{'balance' : total})
    serializer_class = User_objects
class create_user(generics.CreateAPIView):
    queryset = USer_Model.objects.all()
    serializer_class = create_user_serializers

class debt_records(generics.CreateAPIView):
    queryset = Debt_model.objects.all()
    serializer_class = create_debt_serializer
