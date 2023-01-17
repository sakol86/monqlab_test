import requests


payload={"dateStart": "2023-01-15T10:56:17+03:00",
  "dateEnd": "2023-02-15T10:56:17+03:00",
  "title": "Test Service Mode",
  "configItems": [
    {
      "id": 1597,
      "scope": "CiAndChildren",
      "depth": 3
    }
  ],
  "labels": {
    "x1": "y1",
    "x2": "y2"
  }
}
tok= "73786BAB8DF9778254D2B9C3539E3BF2D5E378B8C59C046471E7E09F6A3A500E"
url= "https://xy.acure.io/api/public/sm/v1/rsm-maintenance"
headers = {
            'Accept':'application/json',
           'Authorization': f'Bearer {tok}'
    }

response = requests.request('POST',url, headers=headers,
                            data=payload
                            )

print(response)
print(response.text)
# print(payload)
