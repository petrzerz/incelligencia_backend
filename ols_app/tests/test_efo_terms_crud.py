from faker import Faker
from ols_app.models import EFOTerm

fake = Faker()


def test_post_efo_term(db, api_client):
    request_body = {
        "label": fake.name(),
        "term_id": fake.name(),
        'iri': fake.url()
    }
    response = api_client.post('/api/efoterms', request_body, format='json')
    assert response.status_code == 201
    count = EFOTerm.objects.all().count()
    assert count == 1


def test_get_efo_terms(db, api_client, new_efo_term):
    response = api_client.get('/api/efoterms', format='json')
    assert response.status_code == 200


def test_delete_efo_terms(db, api_client, new_efo_term):
    response = api_client.delete(f'/api/efoterms/{new_efo_term.id}', format='json')
    assert response.status_code == 204
    count = EFOTerm.objects.all().count()
    assert count == 0


def test_patch_efo_terms(db, api_client, new_efo_term):
    request_body = {
        "label": 'patched'
    }
    response = api_client.patch(f'/api/efoterms/{new_efo_term.id}', request_body, format='json')
    assert response.status_code == 200
    patched_field = EFOTerm.objects.get(id=new_efo_term.id).label
    assert patched_field == 'patched'
