import random
from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.shortcuts import render
from utils.tencent.sms import send_sms_single
from utils.wangyi_email.email_163 import send_163_email
from tracer.local_settings import EMAIL_FORMAT,REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_ENCODING


def send_sms(request):
    phone_number = request.phone_number
    code = random.randrange(100000, 999999)
    """
        手机号，模板id，验证码
    """
    send_sms_single(phone_number, 517453, code)
    return HttpResponse("发送成功")


def send_email(request):
    email = request.email
    code = random.randrange(100000, 999999)
    """
        接收邮箱，验证码
    """
    template = None
    if EMAIL_FORMAT['login_url'] in str(request):
        template = "登录"
    elif EMAIL_FORMAT['register_url'] in str(request):
        template = "注册"

    import redis
    conn = redis.Redis(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_ENCODING)
    conn.set(email, code, ex=300)

    data = send_163_email(email, code, template)
    return render(request, 'send_result.html', data)


from django import forms
from web import models

class RegisterModelForm(forms.ModelForm):
    username = forms.CharField(label="用户名", widget=forms.TextInput())
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput())
    mobile_phone = forms.CharField(label="手机号",
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', "手机号格式错误")],
                                   widget=forms.TextInput())
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码", widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = "__all__"
        # 设置顺序
        # fields = ['username', 'email', 'mobile_phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'请输入{field.label}'


def register(request):
    form = RegisterModelForm()
    return render(request, "register.html", {'form': form})
