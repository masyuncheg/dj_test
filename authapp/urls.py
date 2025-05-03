from django.urls import path
from . import views
urlpatterns = [
path('log/', views.auth_form_view, name='login'),
path('reg/', views.reg_form_view, name='register'),
]
