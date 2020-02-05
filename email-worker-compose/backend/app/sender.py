import psycopg2
import redis
import json
import os
from bottle import Bottle, request

class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method = 'POST', callback = self.send)
        
        redis_host = os.getenv('REDIS_HOST', 'queue')
        self.queue = redis.StrictRedis(host = redis_host, port = 6379, db = 0)

        db_host = os.getenv('DB_HOST', 'database')
        db_user = os.getenv('DB_USER', 'postgres')
        db_name = os.getenv('DB_NAME', 'email_sender')
        dsn = f'dbname={db_name} user={db_user} host={db_host}'
        self.db_conn = psycopg2.connect(dsn)

    def store_email(self, subject, message):
        SQL = 'INSERT INTO email (subject, message) VALUES (%s, %s)'

        cursor = self.db_conn.cursor()
        cursor.execute(SQL, (subject, message))

        self.db_conn.commit()

        cursor.close()

        print('Email registered on database')

    def append_email(self, subject, message):
        email = { 'subject': subject, 'message': message }
        self.queue.rpush('sender', json.dumps(email))

        print('Email added to queue!')

    def send(self):
        subject = request.forms.get('subject')
        message = request.forms.get('message')

        self.store_email(subject, message)
        self.append_email(subject, message)

        return 'Queued email! Subject: {} | Message: {}'.format(
            subject, 
            message
        )

if __name__ == '__main__':
    Sender().run(host = '0.0.0.0', port = 8080, debug = True)
    