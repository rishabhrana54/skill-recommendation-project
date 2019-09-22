from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('registerUser',views.registerUser,name='registerUser'),
    path('viewProfile/?P<pk>', views.viewProfile, name='viewProfile'),
    path('editProfile/?P<pk> ',views.editProfile,name='editProfile'),
    path('submitProfile',views.submitProfile,name='submitProfile'),
    path('login',views.loginUser,name='loginUser'),
    path('skillsuser',views.skillsuser,name='skillsuser')
    

] 