from django.urls import path
from personal_portfolio import views

urlpatterns = [    
    path('', views.Home, name='Home'),    
    path('about', views.About, name='About'),
    path('works', views.Works, name='Works'),
    path('contact', views.Contact, name='contact'),
]
