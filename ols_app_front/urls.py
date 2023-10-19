from django.urls import path, include
from rest_framework import routers

from .views import EFOTermTableViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('efotermstable', EFOTermTableViewSet, 'efotermstable')

urlpatterns = [path('', include(router.urls))]
