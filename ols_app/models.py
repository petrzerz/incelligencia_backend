from django.core.exceptions import ValidationError
from django.db import models


class EFOTerm(models.Model):
    term_id = models.CharField(max_length=255, unique=True)
    label = models.CharField()
    iri = models.TextField()

    def __str__(self):
        return f"term_id: {self.term_id}, label: {self.label}"


class EFOTermSynonym(models.Model):
    term = models.ForeignKey(EFOTerm, related_name='synonyms', on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    def __str__(self):
        return f"term_id: {self.term_id}, synonym: {self.synonym}"


class EFOTermDescription(models.Model):
    term = models.ForeignKey(EFOTerm, related_name='descriptions', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"term_id: {self.term_id}, description: {self.description}"


class EFOTermOntology(models.Model):
    parent = models.ForeignKey(EFOTerm, related_name='children', on_delete=models.CASCADE)
    child = models.ForeignKey(EFOTerm, related_name='parents', on_delete=models.CASCADE)

    def is_parent_child_same(self):
        if self.parent == self.child:
            raise ValidationError("Terms can't be parents or children of themselves")

    def save(self, *args, **kwargs):
        self.is_parent_child_same()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"parent_id: {self.parent}, child_id: {self.child}"

    class Meta:
        unique_together = ('parent', 'child')
