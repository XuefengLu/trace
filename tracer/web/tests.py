import redis
from django.test import TestCase

# Create your tests here.


conn = redis.Redis(host='192.168.122.3', port=6379, password="redis", encoding='utf-8')
# conn.set('123456', '9999', ex=10)

print(conn.get('123456'))
