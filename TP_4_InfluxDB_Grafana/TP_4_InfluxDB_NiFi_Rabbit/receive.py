#!/usr/bin/env python
#source https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika, sys, os

def main():
        #Connection to rabbitmq 
        credentials = pika.PlainCredentials('rabbitmq','rabbitmq')
        parameters = pika.ConnectionParameters(host='localhost',port=5672,credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        #t works by subscribing a callback function to a queue. 
        # Whenever we receive a message, this callback function is called by the Pika library.     
        def callback(ch,method,properties,body):
                print(" [x] Reveived %r" % body)
        #Next, we need to tell RabbitMQ that this particular callback function 
        # should receive messages from our client_info queue:
        channel.basic_consume(queue='hello', on_message_callback=callback,auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

if __name__ == '__main__' :
    try : 
        main()
    except KeyboardInterrupt :
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit :
            os._exit(0)