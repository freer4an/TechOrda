import pika


credentials = pika.PlainCredentials('guest', 'guest')
connection_parameter = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(connection_parameter)
channel = connection.channel()

def consumer_callback(channel, method, properties, body):
    print(body)

tag = channel.basic_consume(queue='test1', auto_ack=True, on_message_callback=consumer_callback)
channel.start_consuming()


