from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('dairy/', views.category, {'category_name': 'dairy'}, name='dairy'),
    path('meat/', views.category, {'category_name': 'meat'}, name='meat'),
    path('vegan/', views.category, {'category_name': 'vegan'}, name='vegan'),
    path(
        'chicken-duck-fish/',
        views.category,
        {'category_name': 'chicken-fish'},
        name='chicken_fish',
    ),
    path('contact/', views.contact, name='contact'),
]