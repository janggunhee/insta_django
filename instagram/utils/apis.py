import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from rest_framework.views import APIView

from post.models import Post

"""
class SMSSerializer:
    receiver에 휴대전화 형식의 데이터가 왔는지 validate
    message에 90자 이하의 문자열이 왔는지 validate
    
    is_valid()검사 후 
        serializer.data에 있는 내용을 이용해서 send처리
    
"""

class SendSMS(APIView):
    def post(self, request):
        pass

