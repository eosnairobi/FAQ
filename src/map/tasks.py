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

@shared_task
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

@shared_task
def process_bp_json(bp, data):
    """
        Parses the bp.json file info and saves the lat, long of the BP
    """
    org_details = data.get('org')
    if org_details:
        location = org_details.get('location')
        display_name = org_details.get('candidate_name')
        if display_name:
            bp.display_name = display_name

        if location:
            latitude = location.get('latitude')
            longitude = location.get('longitude')
            bp.latitude, bp.longitude = latitude, longitude
        bp.save()


def get_bp_coords():
    bps = BlockProducer.objects.all()
    for bp in bps:
        pass


"""                    
                         
        {
                         latLng: [41.9, 12.45],
                         name: "Vatican City"
                     }
    
         if bp.latitude and bp.longitude:
             if bp.display_name:
                 name = bp.display_name
             else:
                 name = bp.account_name
             data.append({"latLng":[str(bp.latitude), str(bp.longitude)],"name":name})
             
    with open('longitudes.json', 'w') as file:
    ...:     file.write(json.dumps(data))
    ...:      
         

"""
