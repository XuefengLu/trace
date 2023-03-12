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

# 发送邮件模板
EMAIL_FORMAT = {
    "login_url": "login/send/email/",
    "register_url": "register/send/email/",
    "login": "登录",
    "register": "注册"
}

# redis 配置信息
REDIS_HOST = '192.168.122.3'
REDIS_PORT = 6379
REDIS_PASSWORD = "redis"
REDIS_ENCODING = 'utf-8'
