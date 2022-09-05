from django.urls import path

from .views import index, contact, produto

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('produto/<int:pk>', produto, name='produto')
]
