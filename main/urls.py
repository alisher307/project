from django.urls import path
from .views import *
urlpatterns = [
    path('', index_view, name='index_url'),
    path('create_reservation', create_reservation_view, name='create_reservation'),

]





