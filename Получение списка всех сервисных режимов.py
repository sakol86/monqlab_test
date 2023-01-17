import requests


# payload={}
tok= "73786BAB8DF9778254D2B9C3539E3BF2D5E378B8C59C046471E7E09F6A3A500E"
url= "https://xy.acure.io/api/public/sm/v1/rsm-maintenance"
headers = {
            # 'Accept':'application/json',
           'Authorization': 'Bearer 73786BAB8DF9778254D2B9C3539E3BF2D5E378B8C59C046471E7E09F6A3A500E'
    }

response = requests.request('GET',url, headers=headers,
                            # data=payload
                            )


print(response.text)
# print(payload)