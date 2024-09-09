from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CouponViewSet
 
router = DefaultRouter()
router.register('', CouponViewSet, basename='coupon')
app_name ='coupon'
 
urlpatterns=[
    path('', include(router.urls))
]