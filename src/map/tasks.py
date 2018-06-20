from celery import shared_task
from .models import BlockProducer


def generate_locations():
    bps = BlockProducer.objects.all()
