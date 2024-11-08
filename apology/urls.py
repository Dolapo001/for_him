# apology/urls.py
from django.urls import path
from .views import apology_view, response_view, thank_you_view

urlpatterns = [
    path('', apology_view, name="apology"),
    path('response/', response_view, name="response"),
    path('thank-you/', thank_you_view, name='thank_you'),
]