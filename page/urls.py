from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('science/', views.science, name='science'),
    path('business/', views.business, name='business'),
    path('career/', views.career, name='career'),
    path('product/', views.product, name='product'),
    path('plan/', views.plan, name='plan'),
]
