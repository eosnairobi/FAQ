from celery import shared_task
from .models import BlockProducer
import requests
import json


def generate_locations():
    bps = BlockProducer.objects.all()
    url_list = []
    failed_list = []
    errors = []
    for bp in bps:
        # Get the Urls
        url = '{}/{}'.format(bp.url, 'bp.json')
        try:
            r = requests.get(url)
            if r.status_code == 200:
                url_list.append(bp.url)
                process_bp(json.dumps(r.text))
            else:
                failed_list.append(bp.url)
        except Exception as e:
            errors.append(str(e))
