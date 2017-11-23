from django.conf import settings
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def send_sms(receiver, message):

# set api key, api secret
    api_key = settings.COOLSMS_API_KEY
    api_secret = settings.COOLSMS_API_SECRET
    sender = settings.COOLSMS_SENDER

    ## 4 params(to, from, type, text) are mandatory. must be filled


    params = dict()
    params['type'] = 'sms'
    params['to'] = receiver
    params['from'] = sender
    params['text'] = message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        data = {
            'succes_count': response['success_count'],
            'error_count': response['error']
        }
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)