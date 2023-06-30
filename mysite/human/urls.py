from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('person/', index, name='index'),
    path('person/<int:pk>/', DetailPerson.as_view(), name='person_detail'),
    path('create/', CreatePerson.as_view(), name='create'),
    path('delete/<int:pk>', DeletePerson.as_view(), name='delete'),
    path('update/<int:pk>', UpdatePerson.as_view(), name='update')
]