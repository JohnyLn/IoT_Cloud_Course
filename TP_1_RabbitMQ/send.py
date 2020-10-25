#!/usr/bin/env python
#source https://www.rabbitmq.com/tutorials/tutorial-one-python.html
import pika


#_________________________________________________________________________________________________
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#This tutorial assumes RabbitMQ is installed and running on localhost on the standard port (5672). 
# In case you use a different host, port or credentials, connections settings would require adjusting.
# --> ProbableAuthenticationError: ConnectionClosedByBroker: (403) 'ACCESS_REFUSED - Login was refused 
#_________________________________________________________________________________________________

#https://pika.readthedocs.io/en/stable/modules/parameters.html?fbclid=IwAR17nchrFzL2DyshBkpLjW4DFy4xLJaRwfNKHCfEXSh9YpXV3EiGeGmbgRE

# Set the connection parameters to connect to rabbit-server1 on port 5672
# on the / virtual host using the username "guest" and password "guest"
#credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
#parameters = pika.ConnectionParameters(credentials=credentials)

credentials = pika.PlainCredentials('rabbitmq','rabbitmq')
parameters = pika.ConnectionParameters(host='localhost',port=5672,virtual_host='client1',credentials=credentials)
connection = pika.BlockingConnection(parameters)

#_________________________________________________________________________________________________

#We're connected now, to a broker on the local machine - hence the localhost. 
# If we wanted to connect to a broker on a different machine 
# we'd simply specify its name or IP address here.
channel = connection.channel()

#Create a new queue
# #channel.queue_declare(queue='hello')
#The next step, just like before, is to make sure that the queue exists. 



#We have 2 queues on RabbotMQ, client_info and client_log with a fanout called fanout_first

channel.basic_publish(exchange='fanout_first',routing_key='',body='Hello World! from Python')
print(" [x] Sent 'Hello World! on Python'")

connection.close()

