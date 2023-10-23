import factory
from faker import Faker

from ols_app.models import *

fake = Faker()


class EFOTermFactory(factory.django.DjangoModelFactory):
    term_id = factory.Sequence(lambda n: f'obo-{n}')
    label = fake.name()
    iri = fake.name()

    class Meta:
        model = EFOTerm


class EFOTermSynonymFactory(factory.django.DjangoModelFactory):
    term = factory.SubFactory(EFOTermFactory)
    synonym = fake.name()

    class Meta:
        model = EFOTermSynonym


class EFOTermDescriptionFactory(factory.django.DjangoModelFactory):
    term = factory.SubFactory(EFOTermFactory)
    description = fake.name()

    class Meta:
        model = EFOTermDescription


class EFOTermOntologyFactory(factory.django.DjangoModelFactory):
    parent = factory.SubFactory(EFOTermFactory)
    child = factory.SubFactory(EFOTermFactory)

    class Meta:
        model = EFOTermOntology
