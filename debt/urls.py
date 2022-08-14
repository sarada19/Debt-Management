from django.urls import path
from .views import *

urlpatterns = [
    path('',User_objects.as_view()),
    path('user/<str:name>',User_objects.as_view()),
    path('Create_User', create_user.as_view()),
    path('debt-records', debt_records.as_view()),
]