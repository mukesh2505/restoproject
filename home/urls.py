from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('about/', About.as_view(), name="about"),
    path('menu/', Menu.as_view(), name="menu"),
    path('contact/', Contact.as_view(), name="contact"),
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', Logout.as_view(), name="logout"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('payment/', Payment.as_view(), name="payment"),
    path('success/', Success.as_view(), name="success"),
]
