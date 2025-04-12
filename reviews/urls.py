from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('paper/<slug:paper_slug>/review/', views.review_create, name='create'),
    path('paper/<slug:paper_slug>/reviews/', views.review_list, name='list'),
]
