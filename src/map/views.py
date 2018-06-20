from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import sys
import traceback
from .models import BlockProducer
from django.db import transaction, IntegrityError


EOSNAIROBI_ENDPOINT = 'https://mainnet.eoscanada.com/v1/chain/get_producers'
HEADERS = {'accept': 'application/json', 'content-type': 'application/json'}


@api_view(['GET'])
def query_bps(request):
    try:
        # 500 is a crazy #, but who knows? We could end up with 500 BPCs over time
        resp = requests.post(EOSNAIROBI_ENDPOINT, data=json.dumps({"json": "true", "limit": 500}), headers=HEADERS)
        data = json.loads(resp.text)
        response = data
        if data:
            with transaction.atomic():
                for item in data.get('rows'):
                    bp, created = BlockProducer.objects.update_or_create(account_name=item.get('owner'),
                                                                         producer_key=item.get('producer_key'),
                                                                         url=item.get('url'))

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        response = {'error': str(exc_value)}
    return Response(response)


class BlockProducerObject(object):

    def __init__(self, owner, producer_key, url):
        self.owner = owner
        self.producer_key = producer_key
        self.url = url
