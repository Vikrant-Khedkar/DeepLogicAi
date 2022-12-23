from .views import *
from django.urls import path,include
from knox import views as knox_views
from .views import LoginAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register('data',DataApi)


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('login/',get_pdf,name='login'),
    path('api/',include(router.urls)),
    path('upload/',home,name='upload'),
    path('convert/',test,name='convert'),
    path('converter/',converter,name='converter'),
    path('logout/', logout_view, name='logout'),
    path('display/',TextDisplay,name='display'),
    path('register/',Register,name='register'),
    
]