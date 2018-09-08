import requests
import json

# data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
# data = json.dumps(data)
payload = {'partnerid': 'provedoruno',
					 'cardid': 'provedorunop'}
					 
r = requests.post('http://localhost:8000/api/partnerData',json=payload)
print(r.text)