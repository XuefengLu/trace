import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from utils.tencent.sms import send_sms_single
from utils.wangyi_email.email_163 import send_163_email


def send_sms(request):
    phone_number = request.phone_number
    code = random.randrange(100000, 999999)
    """
        手机号，模板id，验证码
    """
    send_sms_single(phone_number, 517453, code)
    return HttpResponse("发送成功")


def send_email(request):
    # email = request.email
    email = "1936827000@qq.com"
    code = random.randrange(100000, 999999)
    """
        接收邮箱，验证码
    """
    data = send_163_email(email, code)
    return render(request, 'send_result.html', data)
