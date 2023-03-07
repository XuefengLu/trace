LANGUAGE_CODE = 'zh-hans'

# settings.py没有的配置，自己加的
SMS = 66

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.122.3',
        'PORT': 3306
    }
}
