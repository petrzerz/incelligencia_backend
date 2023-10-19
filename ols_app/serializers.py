from rest_framework import serializers

from .models import EFOTerm, EFOTermSynonym, EFOTermOntology


class EFOTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = EFOTerm
        fields = '__all__'


class EFOTermSynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = EFOTermSynonym
        fields = '__all__'


class EFOTermOntologySerializer(serializers.ModelSerializer):
    class Meta:
        model = EFOTermOntology
        fields = '__all__'
