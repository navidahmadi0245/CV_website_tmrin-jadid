from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [


    path('blog', blog_view,name='blog'),
    path('single',single_view,name='single'),

]
