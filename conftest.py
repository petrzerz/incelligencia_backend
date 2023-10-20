import pytest

from pytest_factoryboy import register
from factories import EFOTermFactory, EFOTermSynonymFactory, EFOTermDescriptionFactory, EFOTermOntologyFactory
from rest_framework.test import APIClient
from faker import Faker

fake = Faker()

register(EFOTermFactory)
register(EFOTermSynonymFactory)
register(EFOTermDescriptionFactory)
register(EFOTermOntologyFactory)


@pytest.fixture
def new_efo_term(db, efo_term_factory):
    efo_term = efo_term_factory.create()
    return efo_term


@pytest.fixture
def efo_term_data():
    return {
        "term_id": fake.name(),
        "label": fake.name(),
        "iri": fake.name()
    }


@pytest.fixture
def efo_term_patch_data():
    return {
        'label': 'patched'
    }


@pytest.fixture
def new_efo_term_synonym(db, efo_term_synonym_factory):
    efo_term_synonym = efo_term_synonym_factory.create()
    return efo_term_synonym


@pytest.fixture
def new_efo_term_description(db, efo_term_description_factory):
    efo_term_description = efo_term_description_factory.create()
    return efo_term_description


@pytest.fixture
def new_efo_term_ontology(db, efo_term_ontology_factory):
    efo_term_ontology = efo_term_ontology_factory.create()
    return efo_term_ontology


@pytest.fixture
def api_client():
    return APIClient()
