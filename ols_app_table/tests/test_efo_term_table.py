from faker import Faker

fake = Faker()


def test_get_list_efo_terms_table(db, api_client, new_efo_term, new_efo_term_description, new_efo_term_synonym):
    response = api_client.get('/api/table/efotermstable', format='json')
    assert response.status_code == 200


def test_get_one_efo_terms_table(db, api_client, new_efo_term, new_efo_term_description, new_efo_term_synonym):
    response = api_client.get(f'/api/table/efotermstable/{new_efo_term.id}', format='json')
    assert response.status_code == 200
