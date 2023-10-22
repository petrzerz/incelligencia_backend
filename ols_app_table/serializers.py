from rest_framework import serializers

from ols_app.models import EFOTerm


class EFOTermTableSerializer(serializers.ModelSerializer):
    synonyms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='synonym')
    descriptions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='description')

    class Meta:
        model = EFOTerm
        fields = ['id', 'term_id', 'label', 'iri', 'synonyms', 'descriptions']
