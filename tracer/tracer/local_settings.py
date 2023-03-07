LANGUAGE_CODE = 'zh-hans'

# settings.py没有的配置，自己加的
SMS = 666

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
