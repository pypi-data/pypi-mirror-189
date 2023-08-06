from django.db import models


class Filter(models.Model):
    name = models.CharField(max_length=75)
    model = models.CharField(max_length=256)
    filters = models.JSONField(default=dict)

    sequence = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sequence", "name"]

    def __str__(self):
        return self.name

    @classmethod
    def filters_for_model(cls, model):
        return cls.objects.filter(
            model=f"{model._meta.app_label}.{model._meta.model_name}"
        )
