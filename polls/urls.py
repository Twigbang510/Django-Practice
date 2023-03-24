from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.my_form_view, name="view_form"),
    # path('test/' ,views.testForm, name="test"),
]
