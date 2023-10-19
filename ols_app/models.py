from django.db import models


class EFOTerm(models.Model):
    term_id = models.CharField(max_length=255, unique=True)
    label = models.CharField()
    iri = models.URLField()


class EFOTermSynonym(models.Model):
    term = models.ForeignKey(EFOTerm, related_name='synonyms', on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)


class EFOTermOntology(models.Model):
    parent = models.ForeignKey(EFOTerm, related_name='children', on_delete=models.CASCADE)
    child = models.ForeignKey(EFOTerm, related_name='parents', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('parent', 'child')
