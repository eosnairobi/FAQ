from django.db import models
import uuid


class BlockProducer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account_name = models.CharField(max_length=12)
    producer_key = models.CharField(max_length=60)
    display_name = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    url = models.URLField()
    latitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def get_location(self):
        return self.latitude, self.longitude

    def __str__(self):
        return self.account_name
