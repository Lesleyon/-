import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
channel = connection.channel()
queue_name = 'IKBO-12-21_Shuvalov'
message = "Это одно сообщение для очереди."
channel.basic_publish(exchange='', routing_key=queue_name, body=message)
print(f"Отправлено сообщение: {message}")
connection.close()
