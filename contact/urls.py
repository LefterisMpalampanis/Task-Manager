from django.urls import path
from .views import contact_form_view

urlpatterns = [
    path('', contact_form_view, name='contact_form'),
]
