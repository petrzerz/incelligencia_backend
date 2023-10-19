from django.urls import path, include
from rest_framework import routers

from .views import EFOTermViewSet, EFOTermSynonymViewSet, EFOTermOntologyViewSet, EFOTermDescriptionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('efoterms', EFOTermViewSet, 'efoterms')
router.register('efotermsynonyms', EFOTermSynonymViewSet, 'efotermsynonyms')
router.register('efotermontologies', EFOTermOntologyViewSet, 'efotermontologies')
router.register('efotermdescriptions', EFOTermDescriptionViewSet, 'efotermdescriptions')

urlpatterns = [path('', include(router.urls))]
