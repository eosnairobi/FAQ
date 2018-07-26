import json
import sys
import traceback

import requests

from django.db import IntegrityError, transaction
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BlockProducer

EOSNAIROBI_ENDPOINT = 'https://mainnet.eoscanada.com/v1/chain/get_producers'
HEADERS = {'accept': 'application/json', 'content-type': 'application/json'}


@api_view(['GET'])
def query_bps(request):
    try:
        # 500 is a crazy #, but who knows? We could end up with 500 BPCs over time
        resp = requests.post(EOSNAIROBI_ENDPOINT, data=json.dumps(
            {"json": "true", "limit": 500}), headers=HEADERS)
        data = json.loads(resp.text)
        response = data
        if data:
            with transaction.atomic():
                for item in data.get('rows'):
                    bp, created = BlockProducer.objects.update_or_create(account_name=item.get('owner'),
                                                                         producer_key=item.get(
                                                                             'producer_key'),
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


@api_view(['GET'])
def bp_data(request):
    bps = BlockProducer.objects.all()
    response = {}
    points = []
    for bp in bps:
        # {latLng: [41.50, -87.37], name: 'Chicago'},
        if bp.display_name:
            display_name = bp.display_name
        else:
            display_name = bp.account_name
        points.append(
            {'latLng': [bp.latitude, bp.longitude], 'name': display_name})
    return Response(points)


def view_map(request):
    return render(request, 'test_map.html')
