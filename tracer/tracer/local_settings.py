LANGUAGE_CODE = 'zh-hans'

# settings.py没有的配置，自己加的
SMS = 666

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tracer',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.122.3',
        'PORT': 3306
    }
}

MAIL_USER = "feng667298@163.com"  # 用户名
MAIL_PASS = "VDJQLAIWPFWGDRNU"  # 163授权码
SENDER = "feng667298@163.com"  # 发送方
MAIL_HOST = "smtp.163.com"  # 设置服务器
MAIL_PORT = 25  # 端口号

