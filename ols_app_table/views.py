from ols_app.models import EFOTerm
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import EFOTermTableSerializer
from ols.pagination_decorator import paginate


class EFOTermTableViewSet(viewsets.ModelViewSet):
    serializer_class = EFOTermTableSerializer
    resource_name = 'efotermtabe'
    http_method_names = ['get']

    @paginate
    @action(detail=True)
    def parents(self, request, pk=None):
        return EFOTerm.objects.filter(children__child=pk)

    @paginate
    @action(detail=True)
    def children(self, request, pk=None):
        return EFOTerm.objects.filter(parents__parent=pk)

    def get_queryset(self):
        return EFOTerm.objects.all()
