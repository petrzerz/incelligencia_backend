from faker import Faker
from ols_app.models import EFOTermSynonym

fake = Faker()


def test_post_efo_term_synonym(db, api_client, new_efo_term):
    payload = {
        "synonym": fake.name(),
        "term": new_efo_term.id
    }
    response = api_client.post('/api/efotermsynonyms', payload, format='json')
    assert response.status_code == 201
    count = EFOTermSynonym.objects.all().count()
    assert count == 1


def test_get_efo_term_synonym(db, api_client, new_efo_term_synonym):
    response = api_client.get('/api/efotermsynonyms', format='json')
    assert response.status_code == 200


def test_delete_efo_term_synonym(db, api_client, new_efo_term_synonym):
    response = api_client.delete(f'/api/efotermsynonyms/{new_efo_term_synonym.id}', format='json')
    assert response.status_code == 204
    count = EFOTermSynonym.objects.all().count()
    assert count == 0


def test_patch_efo_term_synonym(db, api_client, new_efo_term_synonym):
    payload = {
        "synonym": "patched"
    }
    response = api_client.patch(f'/api/efotermsynonyms/{new_efo_term_synonym.id}', payload, format='json')
    assert response.status_code == 200
    patched_field = EFOTermSynonym.objects.get(id=new_efo_term_synonym.id).synonym
    assert patched_field == 'patched'
