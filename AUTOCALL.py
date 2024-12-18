from twilio.rest import Client
# from urllib.parse import urlencode
import time

SID = 'AC67ae33854f5c9004efee994a2c89e22f'
token='55327d6b048dd164c27c8f008372b96b'
client = Client(SID, token)
client.messages.create(body="How are you?",from_='+17756181527', to='+918124583979')

while(True):

    account_sid = 'AC67ae33854f5c9004efee994a2c89e22f'
    auth_token = '55327d6b048dd164c27c8f008372b96b'

    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml='<Response><Say>Hello keerthi how are you</Say></Response>',
                            to='+918610951743',
                            from_='+17756181527',
                            # url = 'https://handler.twilio.com/twiml/EHfbb90737b757304c9b3cbcb81ba73770?' + urlencode({'Message': "Incident INC12345 assigned to you "})
                            #url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770'

                        )

    print(call.sid)
    call_sid = call.sid

    time.sleep(25)

    call = client.calls(call_sid).fetch()
    print(call.status)

    if('complete' in call.status):
        print("call answered breaking loop ")
        break
    else:
        print("retrying again")

