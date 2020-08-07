from django.urls import path
from course import views 
from .views import HomeView

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',HomeView.as_view(),name='home'),
    
    
]
