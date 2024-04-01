from django.urls import path
from . import views
from .views import viewclass,viewclass2,viewclass3
urlpatterns = [
    path('',views.link1,name = 'link1'),
    path('home1/',viewclass.as_view()),
    path('home2/',viewclass2.as_view()),
    path('home3/',viewclass3.as_view())
]
