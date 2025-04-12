from django.urls import path
from . import views

app_name = 'papers'

urlpatterns = [
    path('', views.paper_list, name='list'),
    path('submit/', views.paper_submit, name='submit'),
    path('category/<slug:slug>/', views.paper_list, name='category'),
    path('tag/<slug:tag_slug>/', views.paper_list, name='tag'),
    path('<slug:slug>/', views.paper_detail, name='detail'),
]
