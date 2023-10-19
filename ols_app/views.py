from rest_framework import viewsets
from .models import EFOTerm, EFOTermSynonym, EFOTermOntology
from .serializers import EFOTermSerializer, EFOTermSynonymSerializer, EFOTermOntologySerializer


# Create your views here.
class EFOTermViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermSerializer
    resource_name = 'efoterms'

    def get_queryset(self):
        return EFOTerm.objects.all()


class EFOTermSynonymViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermSynonymSerializer
    resource_name = 'efotermsynonym'

    def get_queryset(self):
        return EFOTermSynonym.objects.all()


class EFOTermOntologyViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermOntologySerializer
    resource = 'efotermontologies'

    def get_queryset(self):
        return EFOTermOntology.objects.all()
