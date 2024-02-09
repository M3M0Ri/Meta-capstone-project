"""littlelemon URL Configuration """

from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from restaurant import views 

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')) 
]
