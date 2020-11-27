from django.urls import path
from . import views
from account.api.views import *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


app_name="api_account"

urlpatterns=[
path('login', obtain_auth_token, name='api_token_auth'),
path('signup',views.registration_view,name="api_register"),
path('userdetails',views.api_user_details,name='userdetails'),
path('profiledetails',views.api_profile_details,name='profiledetails'),

]
