from faker import Faker
from ols_app.models import EFOTermOntology
import pytest

fake = Faker()


def test_post_efo_term_ontologies(db, api_client, new_efo_term, new_efo_term_2):
    payload = {
        "parent": new_efo_term.id,
        "child": new_efo_term_2.id
    }
    response = api_client.post('/api/efotermontologies', payload, format='json')
    assert response.status_code == 201
    count = EFOTermOntology.objects.all().count()
    assert count == 1


def test_get_efo_term_synonym(db, api_client, new_efo_term_ontology):
    response = api_client.get('/api/efotermontologies', format='json')
    assert response.status_code == 200


def test_delete_efo_term_synonym(db, api_client, new_efo_term_ontology):
    response = api_client.delete(f'/api/efotermontologies/{new_efo_term_ontology.id}', format='json')
    assert response.status_code == 204
    count = EFOTermOntology.objects.all().count()
    assert count == 0


def test_patch_efo_term_synonym(db, api_client, new_efo_term_ontology, new_efo_term):
    payload = {
        "parent": new_efo_term.id
    }
    response = api_client.patch(f'/api/efotermontologies/{new_efo_term_ontology.id}', payload, format='json')
    assert response.status_code == 200
    patched_field = EFOTermOntology.objects.get(id=new_efo_term_ontology.id).parent.id
    assert patched_field == new_efo_term.id


def test_post_efo_term_ontologies_same_parent_child(db, api_client, new_efo_term, new_efo_term_2):
    payload = {
        "parent": new_efo_term.id,
        "child": new_efo_term.id
    }
    response = api_client.post('/api/efotermontologies', payload, format='json')
    assert response.status_code == 400
    assert response.data[0] == "Terms can't be parents or children of themselves"


def test_post_efo_term_ontologies_only_one_field(db, api_client, new_efo_term):
    request_body = {
        "parent": new_efo_term.id
    }
    response = api_client.post('/api/efotermontologies', request_body, format='json')
    assert response.status_code == 400
