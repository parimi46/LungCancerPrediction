from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('base',views.base,name="base"),
    path('user_profile', views.user_profile, name='user_profile'),
    path('predict',views.predict,name="predict"),
    path('results',views.results,name="results")
]