import socket
import pika
import time
hostname = socket.gethostname()
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='nodes')

for i in xrange(20):
    body = "Hello i am from {} - msg: {}".format(hostname, i)
    channel.basic_publish(exchange='', routing_key="nodes", body=body)
    print "Published {}".format(body)
    time.sleep(1)
channel.close()
