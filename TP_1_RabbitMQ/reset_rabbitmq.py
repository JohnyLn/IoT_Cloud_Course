from pyrabbit.api import Client
#https://github.com/bkjones/pyrabbit
#https://rawcdn.githack.com/rabbitmq/rabbitmq-management/v3.8.9/priv/www/api/index.html
#pip3 install pyrabbit
#https://pyrabbit.readthedocs.io/en/latest/
#https://pyrabbit.readthedocs.io/en/latest/api.html
#https://github.com/bkjones/pyrabbit/blob/master/pyrabbit/api.py

new_client =""

#global variable
cl = Client('localhost:15672','rabbitmq','rabbitmq')
cl.is_alive()

def main():
    #Pyrabbit api

    dic_vh = cl.get_vhost_names()
    delete_vh(dic_vh)


def delete_vh(dic_vh):
    """
    Delete each vh in the dic    """
    for _ in dic_vh: 
        try :
            if(_ != "/"):
                cl.delete_vhost(_)
                print("[x] Virtual Host : "+ _ + " a été supprimé")
        except :
            print("/!\ Virtual Host : "+ _ + " n'a pas été supprimé")


if __name__ == '__main__' :
    try : 
        new_client = main()
        deploy_new_client(new_client)
    except KeyboardInterrupt :
        print('INterrupted')
        try:
            sys.exit(0)
        except SystemExit :
            OS._exit(0)


#client_global = input("Enter le nom du nouveau client")

#cl.create_vhost('example_vhost')
#cl.delete_vhost('example_vhost')