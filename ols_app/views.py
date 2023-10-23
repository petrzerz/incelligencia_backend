from rest_framework import viewsets, status

from .models import EFOTerm, EFOTermSynonym, EFOTermOntology, EFOTermDescription
from .serializers import EFOTermSerializer, EFOTermSynonymSerializer, EFOTermOntologySerializer, \
    EFOTermDescriptionSerializer
from rest_framework.response import Response
from rest_framework import serializers


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


class EFOTermDescriptionViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermDescriptionSerializer
    resource_name = 'efotermdescriptions'

    def get_queryset(self):
        return EFOTermDescription.objects.all()


class EFOTermOntologyViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermOntologySerializer
    resource = 'efotermontologies'

    def get_queryset(self):
        return EFOTermOntology.objects.all()
