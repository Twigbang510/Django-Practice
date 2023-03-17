from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.viewList, name="view_list"),
    path('', views.main, name="index" ),
    path('form/',views.viewForm, name="view_form"),
    path('test/' ,views.testForm, name="test"),
]