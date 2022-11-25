from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('result/<str:pays>/<str:ville>',views.result_view, name = 'result'),
]
