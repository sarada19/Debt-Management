from rest_framework import serializers
from .models import *

class create_user_serializers(serializers.ModelSerializer):
    class Meta:
        model = USer_Model
        fields = ['name', 'owes', 'owed_by', 'balance']

class create_debt_serializer(serializers.ModelSerializer):
    class Meta:
        model = Debt_model
        fields = ['lender', 'borrower', 'amount']

class owes_objects(serializers.ModelSerializer):
    class Meta:
        model = owes_Model
        fields = ['name', 'amount']

class owed_by_objects(serializers.ModelSerializer):
    class Meta:
        model = owed_by_Model
        fields = ['name', 'amount']

class User_objects(serializers.ModelSerializer):
    owes = owes_objects(many = True)
    owed_by = owed_by_objects(many = True)
    class Meta:
        model = USer_Model
        fields = ['name', 'owes', 'owed_by', 'balance']
