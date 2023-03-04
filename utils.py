from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('7A7068384D466A644A2B654655713942544B72646A3151474962656F324364784B7A6A45554776684553773D')
        parms = {
            'sender':'',
            'receptor':phone_number,
            'message':f'{code}your verified code'
        }
        response = api.sms_send(parms)
        print(response)

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)



class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin