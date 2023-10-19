from rest_framework import serializers

from ols_app.models import EFOTerm


class EFOTermTableSerializer(serializers.ModelSerializer):
    synonyms_arr = serializers.ListField()
    description_arr = serializers.ListField()

    class Meta:
        model = EFOTerm
        fields = ['id', 'label', 'iri', 'description_arr', 'synonyms_arr']
