from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='ShopHome'),
    path('about/', views.about,name='About'),
    path('contact/', views.contact,name='ContactUs'),
    path('tracker/', views.tracker,name='Tracking'),
    path('search/', views.search,name='search'),
    path('products/<int:myid>', views.productview,name='ProductView'),
    path('checkout/', views.checkout,name='Checkout'),
]