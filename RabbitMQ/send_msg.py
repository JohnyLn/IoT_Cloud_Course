#!/usr/bin/env python
#source https://www.rabbitmq.com/tutorials/tutorial-two-python.html
import pika,sys



credentials = pika.PlainCredentials('rabbitmq','rabbitmq')
parameters = pika.ConnectionParameters(host='localhost',port=5672,virtual_host='client1',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#_________________________________________________________________________________________________
#We have 2 queues on RabbotMQ, client_info and client_log with a fanout called fanout_first


message = ' '.join(sys.argv[1:]) or "Hello World !"
channel.basic_publish(exchange='fanout_first',routing_key='sensor_msg',body=message)
print(" [x] Sent %r" % message)

connection.close()

