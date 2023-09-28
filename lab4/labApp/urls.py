from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:num>",views.calctax, name="taxcalculater"),
    path("TaxRate", views.htmlfile, name='print tax')
]
