from ols_app.models import EFOTerm


def test_post_efo_term(db, api_client, efo_term_data):
    response = api_client.post('/api/efoterms', efo_term_data, format='json')
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


def test_patch_efo_terms(db, api_client, new_efo_term, efo_term_patch_data):
    response = api_client.patch(f'/api/efoterms/{new_efo_term.id}', efo_term_patch_data, format='json')
    assert response.status_code == 200
    patched_field = EFOTerm.objects.get(id=new_efo_term.id).label
    assert patched_field == 'patched'
