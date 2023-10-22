import os

import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "ols.settings")
django.setup()

from ols_app.models import EFOTerm, EFOTermSynonym, EFOTermOntology, EFOTermDescription

visited_nodes = set()


def traverse_children(url, parent_term=None):
    response = requests.get(url)
    data = response.json()

    if "_embedded" in data and "terms" in data["_embedded"]:
        terms = data["_embedded"]["terms"]
        for term in terms:
            if term["iri"] not in visited_nodes:
                visited_nodes.add(term["iri"])
                term_obj, created = EFOTerm.objects.get_or_create(
                    term_id=term["obo_id"],
                    label=term["label"],
                    iri=term["iri"]
                )

                if parent_term is not None:
                    EFOTermOntology.objects.get_or_create(parent=parent_term, child=term_obj)

                if term['synonyms']:
                    create_synonyms(term['synonyms'], term_obj)

                if term['description']:
                    create_description(term['description'], term_obj)

                if "_links" in term and "children" in term["_links"]:
                    child_url = term["_links"]["children"]["href"]
                    traverse_children(child_url, term_obj)


def create_synonyms(synonyms, term_obj):
    for synonym in synonyms:
        EFOTermSynonym.objects.get_or_create(
            term=term_obj,
            synonym=synonym
        )


def create_description(descriptions, term_obj):
    for description in descriptions:
        EFOTermDescription.objects.get_or_create(
            term=term_obj,
            description=description
        )


url = "https://www.ebi.ac.uk/ols/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FIAO_0000030/parents"

traverse_children(url)
