from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('places/<place>',views.Places,name='places')
    # path('',views.index,name='index').
]
