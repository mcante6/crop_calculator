from django.urls import path
from .views import crop_calculator, results

app_name = 'calculations'

urlpatterns = [
    path('', crop_calculator, name='crop_calculator'),
    path('results/', results, name='results'),
]