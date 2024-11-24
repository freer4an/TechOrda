import pika
import pika.connection


credentials = pika.PlainCredentials('guest', 'guest')
connection_parameter = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(connection_parameter)
channel = connection.channel()

msg = "Hello world!"
channel.basic_publish(exchange='', routing_key='test1', body=msg)

connection.close()