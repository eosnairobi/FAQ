from celery import shared_task
from .models import BlockProducer
import requests
import json

"""
{
  "producer_account_name": "eosnairobike",
  "producer_public_key": "EOS54UAELQVaMrc1y98W7KsfLbBchvsQg7FCEYpoiQLi5y1Gvyqcy",
  "org": {
    "candidate_name": "eosnairobike",
    "website": "http://www.eosnairobi.io/",
    "code_of_conduct":"https://steemit.com/eos/@eosnairobi/eosnairobi-block-producer-code-of-conduct-v1-0",
    "email":"blocks@eosnairobi.io",
    "branding":{
      "logo_256":"https://github.com/eosnairobi/bp_info/blob/master/EOSBPlisting/logo256.png",
      "logo_1024":"https://github.com/eosnairobi/bp_info/blob/master/EOSBPlisting/logo1024.png",
      "logo_svg":"https://github.com/eosnairobi/bp_info/blob/master/EOSBPlisting/logo.svg"
    },
    "location": {
      "name": "East Africa",
      "country": "KE",
      "latitude": 0.0236,
      "longitude": 37.9062
    },
    "social": {
      "steemit": "@eosnairobi",
      "twitter": "@EosNairobi",
      "youtube": "channel/UCyNo-qXKUMPxhIrt2TUTtgg",
      "facebook": "",
      "github":"eosnairobi",
      "reddit": "",
      "keybase": "eosnairobi",
      "telegram": "eosnairobi",
      "wechat":""
    }
  },
  "nodes": [
    {
      "location": {
        "name": "Nairobi",
        "country": "KE",
        "latitude": 1.3281,
        "longitude": 36.8666
      },
      "is_producer": false,
      "p2p_endpoint": "",
      "api_endpoint": "",
      "ssl_endpoint": ""
    },
    {
      "location": {
        "name": "",
        "country": "",
        "latitude": "",
        "longitude": ""
      },
      "is_producer": false,
      "p2p_endpoint": "",
      "api_endpoint": "",
      "ssl_endpoint": ""
    },
    {
      "location": {
        "name": "",
        "country": "",
        "latitude": "",
        "longitude": ""
      },
      "is_producer": false,
      "p2p_endpoint": "",
      "api_endpoint": "",
      "ssl_endpoint": ""
    }
  ]
}


"""


@
def obtain_bp_json():
    """ 
        Task to run every midnight, to update the state of the BP Locations
    """
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
                process_bp_json(bp, json.loads(r.text))
            else:
                failed_list.append(bp.url)
        except Exception as e:
            errors.append(str(e))


def process_bp_json(bp, data):
    """
        Parses the bp.json file info and saves the lat, long of the BP
    """
    org_details = data.get('org')
    if org_details:
        location = org_details.get('location')
        if location:
            latitude = location.get('latitude')
            longitude = location.get('longitude')
            bp.latitude, bp.longitude = latitude, longitude
            bp.save()
