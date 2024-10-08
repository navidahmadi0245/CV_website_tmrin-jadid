from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [

    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('services', services_view, name='services'),
    path('elements', elements_view, name='elements'),
    path('portfolio', portfolio_view, name='portfolio'),

    path('test', test_view, name='test'),

]
