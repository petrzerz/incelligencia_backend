from rest_framework import viewsets
from django.contrib.postgres.aggregates import ArrayAgg

from .serializers import EFOTermTableSerializer
from ols_app.models import EFOTerm


class EFOTermTableViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermTableSerializer
    resource_name = 'efotermtabe'

    def get_queryset(self):
        return EFOTerm.objects.annotate(
            description_arr=ArrayAgg('descriptions__description'), synonyms_arr=ArrayAgg('synonyms__synonym'), )
