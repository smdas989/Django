from django.urls import path
from .views import Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('show_detail/',Register.as_view(),name='show_detail')
]