from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.su1),
    path('home1/', views.su2),
    path('home2/', views.su3, name="home2"),
    path('home3/', views.su4),
    path('home4/',views.su5, name="home4"),
    path('home44/', views.su55, name="home44"),
    path('home5/', views.su6),
    path('home6/', views.su7, name="home6"),
    path('home7/<int:id>', views.su8, name="home7"),
    # path('home3/home6', views.su9),
    # path('home4/home6', views.su9),
    path('home3/', views.su4, name="home3"),
    path('home8/', views.su10),
    path('home3/home8/', views.su10),
    path('home9/<int:id>', views.su11, name="home9"),
    path('home10/<int:id>', views.su12, name="home10"),




]