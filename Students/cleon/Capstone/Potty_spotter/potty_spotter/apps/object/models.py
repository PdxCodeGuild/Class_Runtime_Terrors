from django.db import models
from django.utils.translation import ugettext_lazy as _
from models_extensions.models import TimeStampedModel, ActivatorModel
from potty_spotter.core.utils import random_string_generator


class Restroom(TimeStampedModel):
    restroom_id = models.CharField(max_length=20, blank=True, unique=True)
    created_by = models.ForeignKey(
        "user.User", verbose_name=_("Created by"),
        on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)

    class StatusChoices(models.IntegerChoices):
        PENDING = 1, "PENDING"
        APPROVED = 2, "APPROVED"
        REJECTED = 3, "REJECTED"
    status = models.IntegerField(
        _("Status"),
        default=StatusChoices.PENDING,
        choices=StatusChoices.choices,
        blank=True
    )

    def __str__(self):
        return f"{self.restroom_id} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.restroom_id:
            unique_id = random_string_generator(size=12)
            while Restroom.objects.filter(restroom_id=unique_id).exists():
                unique_id = random_string_generator(size=12)
            self.restroom_id = unique_id
        super(Restroom, self).save(*args, **kwargs)
