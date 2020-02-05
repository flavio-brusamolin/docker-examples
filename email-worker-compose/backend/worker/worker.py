import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    queue = redis.Redis(host = redis_host, port = 6379, db = 0)

    print('Waiting for emails...')

    while True:
        email = json.loads(queue.blpop('sender')[1])

        # Simulating email sending
        print('Sending email >', email['subject'])
        sleep(randint(15, 45))
        print('Email sent >', email['subject'])