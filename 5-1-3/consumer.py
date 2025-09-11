import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
queue_name = 'IKBO-12-21_Shuvalov'
channel.queue_declare(queue=queue_name, auto_delete=True)
def callback(ch, method, properties, body):
    print(f"Получено сообщение: {body.decode()}")
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(f"Ожидание сообщений из очереди: {queue_name}")
channel.start_consuming()
