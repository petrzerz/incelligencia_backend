from rest_framework import routers
from django.urls import path, include

from .views import EFOTermViewSet, EFOTermSynonymViewSet, EFOTermOntologyViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('efoterms', EFOTermViewSet, 'efoterms')
router.register('efotermsynonyms', EFOTermSynonymViewSet, 'efotermsynonyms')
router.register('efotermontologies', EFOTermOntologyViewSet, 'efotermontologies')

urlpatterns = [path('', include(router.urls))]
