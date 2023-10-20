from faker import Faker
from ols_app.models import EFOTermDescription

fake = Faker()


def test_post_efo_term_description(db, api_client, new_efo_term):
    request_body = {
        "description": fake.name(),
        "term": new_efo_term.id
    }
    response = api_client.post('/api/efotermdescriptions', request_body, format='json')
    assert response.status_code == 201
    count = EFOTermDescription.objects.all().count()
    assert count == 1


def test_get_efo_term_synonym(db, api_client, new_efo_term_description):
    response = api_client.get('/api/efotermdescriptions', format='json')
    assert response.status_code == 200


def test_delete_efo_term_synonym(db, api_client, new_efo_term_description):
    response = api_client.delete(f'/api/efotermdescriptions/{new_efo_term_description.id}', format='json')
    assert response.status_code == 204
    count = EFOTermDescription.objects.all().count()
    assert count == 0


def test_patch_efo_term_synonym(db, api_client, new_efo_term_description):
    payload = {
        "description": "patched"
    }
    response = api_client.patch(f'/api/efotermdescriptions/{new_efo_term_description.id}', payload, format='json')
    assert response.status_code == 200
    patched_field = EFOTermDescription.objects.get(id=new_efo_term_description.id).description
    assert patched_field == 'patched'
